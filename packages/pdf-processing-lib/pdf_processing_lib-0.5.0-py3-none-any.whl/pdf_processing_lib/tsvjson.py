import os
import json
import hashlib
import random
import pandas as pd
import re
from joblib import Parallel, delayed
from time import time
import gc
from tqdm import tqdm

class TSVJSON:
    def __init__(self, root_directory):
        self.root_directory = root_directory
        self.processed_json_files = []
        self.total_files = 0
        self.processed_files = 0

    def generate_hash(self):
        random_string = str(random.randint(0, 1000000))
        return hashlib.md5(random_string.encode()).hexdigest()[:16]

    @staticmethod
    def classify_class_name(class_name):
        if pd.isnull(class_name) or class_name == "":
            return "Blank"
        elif "MarginText" in class_name:
            return "Margin"
        elif class_name == "MainZone-Head" or "Title" in class_name:
            if class_name not in ["RunningTitleZone", "PageTitleZone-Index"]:
                return "Special"
        return "Regular"

    @staticmethod
    def split_text(text, max_words=400):
        sentences = re.split(r'(?<=[.!?])\s+', text)
        chunks = []
        current_chunk = []
        current_word_count = 0

        for sentence in sentences:
            sentence_word_count = len(sentence.split())
            if current_word_count + sentence_word_count > max_words and current_chunk:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_word_count = 0
            
            current_chunk.append(sentence)
            current_word_count += sentence_word_count

        if current_chunk:
            chunks.append(' '.join(current_chunk))

        return chunks

    def count_total_files(self):
        """Count total TSV files to process for progress tracking"""
        total = 0
        for subdir, _, files in os.walk(self.root_directory):
            if subdir.endswith("final") and "_output" in subdir:
                total += len([f for f in files if f.endswith('.tsv')])
        return total

    def process_single_file(self, file_path, document_name):
        """Process a single TSV file with error handling"""
        try:
            df = pd.read_csv(file_path, sep='\t', encoding='utf-8')
            return len(df)
        except Exception as e:
            print(f"Error processing file {file_path}: {str(e)}")
            return 0

    def parse_tsvs_to_json(self, directory):
        try:
            tsv_files = sorted([f for f in os.listdir(directory) if f.endswith('.tsv')],
                             key=lambda x: int(re.search(r'combined_page(\d+).tsv', x).group(1)))
            
            if not tsv_files:
                return None, 0

            full_document_name = os.path.basename(os.path.dirname(directory))
            document_name = full_document_name.replace("_output", "")
            json_data = []
            current_section = None
            current_text = ""
            current_chunk_pages = []
            
            for file_name in tsv_files:
                try:
                    page_number = re.search(r'combined_page(\d+).tsv', file_name).group(1)
                    file_path = os.path.join(directory, file_name)
                    
                    # Process file content
                    df = pd.read_csv(file_path, sep='\t', encoding='utf-8')
                    df['Category'] = df['class_name'].apply(self.classify_class_name)
                    df['text'] = df['text'].astype(str)
                    
                    for _, row in df.iterrows():
                        category = row['Category']
                        text = row['text'].strip()
                        
                        if category in ["Blank", "Margin"]:
                            json_data.append({
                                "section": text,
                                "text": text,
                                "pages": [page_number],
                                "document": document_name,
                                "word_count": len(text.split()),
                                "hash": self.generate_hash()
                            })
                        elif category == "Special":
                            if current_section is not None and current_text:
                                for chunk in self.split_text(current_text):
                                    json_data.append({
                                        "section": current_section,
                                        "text": chunk,
                                        "pages": current_chunk_pages,
                                        "document": document_name,
                                        "word_count": len(chunk.split()),
                                        "hash": self.generate_hash()
                                    })
                            current_section = text
                            current_text = ""
                            current_chunk_pages = [page_number]
                        else:
                            if current_section is None:
                                current_section = text
                            current_text = current_text + " " + text if current_text else text
                            if page_number not in current_chunk_pages:
                                current_chunk_pages.append(page_number)
                    
                    # Update progress
                    self.processed_files += 1
                    if self.processed_files % 30 == 0:
                        print(f"Processed {self.processed_files}/{self.total_files} files ({(self.processed_files/self.total_files)*100:.1f}%)")
                    
                except Exception as e:
                    print(f"Error processing file {file_name}: {str(e)}")
                    continue

            # Save JSON file
            json_file_name = f"{document_name}.json"
            json_file_path = os.path.join(directory, json_file_name)
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(json_data, json_file, indent=4, ensure_ascii=False)
            
            self.processed_json_files.append(json_file_path)
            return json_file_path, len(tsv_files)
            
        except Exception as e:
            print(f"Error processing directory {directory}: {str(e)}")
            return None, 0

    def process_all_final_directories(self):
        print("Step 1: Processing TSV files to JSON...")
        final_directories = []
        for subdir, dirs, files in os.walk(self.root_directory):
            if subdir.endswith("final") and "_output" in subdir:
                final_directories.append(subdir)
        
        if not final_directories:
            print("No final directories found for TSV processing.")
            return 0, 0, 0

        # Count total files for progress tracking
        self.total_files = self.count_total_files()
        print(f"Found {self.total_files} TSV files to process in {len(final_directories)} directories")

        start_time = time()
        results = []
        
        # Process directories with progress bar
        with tqdm(total=len(final_directories), desc="Processing directories") as pbar:
            for directory in final_directories:
                result = self.parse_tsvs_to_json(directory)
                if result[0]:  # Only append if processing was successful
                    results.append(result)
                pbar.update(1)
                
                # Perform garbage collection every 10 directories
                if len(results) % 10 == 0:
                    gc.collect()
                    
        end_time = time()
        
        total_files_processed = sum(count for _, count in results if count)
        total_time = end_time - start_time
        avg_time_per_file = total_time / total_files_processed if total_files_processed > 0 else 0
        
        print(f"\nProcessed {len(final_directories)} final directories")
        print(f"Successfully processed {total_files_processed}/{self.total_files} files")
        print(f"Total processing time: {total_time:.2f} seconds")
        print(f"Average time per file: {avg_time_per_file:.4f} seconds")

        return total_files_processed, total_time, avg_time_per_file

    def merge_json_files(self, output_file):
        print("\nStep 2: Merging all JSON files...")
        combined_data = []
        total_json_files = len(self.processed_json_files)
        
        with tqdm(total=total_json_files, desc="Merging JSON files") as pbar:
            for json_file in self.processed_json_files:
                try:
                    with open(json_file, 'r') as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            combined_data.extend(data)
                        elif isinstance(data, dict):
                            combined_data.append(data)
                except Exception as e:
                    print(f"Error processing {json_file}: {str(e)}")
                pbar.update(1)

        # Save merged JSON
        try:
            with open(output_file, 'w') as f:
                json.dump(combined_data, f, indent=2, ensure_ascii=False)
            print(f"\nCombined JSON has been written to {output_file}")
            print(f"Total entries in merged file: {len(combined_data)}")
            return output_file, len(combined_data)
        except Exception as e:
            print(f"Error saving merged JSON: {str(e)}")
            return None, 0

    def process(self, final_output_file):
        """
        Main method to run the complete processing pipeline with improved error handling and progress tracking.
        """
        if not os.path.isdir(self.root_directory):
            print("The specified directory does not exist.")
            return None

        print(f"Starting complete document processing pipeline for: {self.root_directory}")
        
        try:
            # Step 1: Process all TSV files to JSON
            tsv_stats = self.process_all_final_directories()
            
            # Step 2: Merge all JSON files
            json_stats = self.merge_json_files(final_output_file)
            
            print("\nProcessing completed!")
            print(f"Final output file: {final_output_file}")
            print(f"Total TSV files processed: {tsv_stats[0]}")
            print(f"Total entries in final merged JSON: {json_stats[1]}")
            
            return {
                "final_output_file": final_output_file,
                "tsv_files_processed": tsv_stats[0],
                "total_processing_time": tsv_stats[1],
                "avg_time_per_file": tsv_stats[2],
                "total_json_entries": json_stats[1]
            }
        except Exception as e:
            print(f"Error in processing pipeline: {str(e)}")
            return None