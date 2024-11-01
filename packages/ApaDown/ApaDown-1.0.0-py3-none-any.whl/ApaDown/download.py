import requests
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import unquote, urlparse
from pathlib import Path
from tqdm import tqdm


class DownloadError(Exception):
    """Custom exception for download errors"""
    def __init__(self, message, url=None, status_code=None):
        self.message = message
        self.url = url
        self.status_code = status_code
        super().__init__(self.message)

    def __str__(self):
        details = []
        if self.url:
            details.append(f"URL: {self.url}")
        if self.status_code:
            details.append(f"Status Code: {self.status_code}")
        
        if details:
            return f"{self.message} ({' | '.join(details)})"
        return self.message


class LinksFileException(Exception):
    """Raised when there's an error fetching links"""
    def __init__(self, message="No links file provided"):
        self.message = message
        super().__init__(self.message)


def get_filename_from_url(url):
    """Extract filename from URL and decode it"""
    parsed = urlparse(url)
    filename = os.path.basename(unquote(parsed.path))
    return filename if filename else 'downloaded_file'


def download_file(url, output_dir, chunk_size=8192, resume_file=None):
    """
    Download a single file with progress bar and support for pause/resume
    
    Args:
        url (str): URL of the file to download
        output_dir (str): Directory to save the file
        chunk_size (int): Size of chunks to download
        resume_file (str): Path to the partially downloaded file (if any)
    
    Returns:
        tuple: (success (bool), filename (str), error message (str) or None)
    """
    try:
        # Check if the file is partially downloaded
        if resume_file:
            start_byte = os.path.getsize(resume_file)
            headers = {'Range': f'bytes={start_byte}-'}
        else:
            start_byte = 0
            headers = {}

        # Send HEAD request first to get file size
        response = requests.head(url, allow_redirects=True)
        file_size = int(response.headers.get('content-length', 0))

        # Get filename from URL
        filename = get_filename_from_url(url)
        output_path = Path(output_dir) / filename

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Download with progress bar
        response = requests.get(url, stream=True, allow_redirects=True, headers=headers)
        response.raise_for_status()

        with tqdm(total=file_size, unit='B', unit_scale=True, 
                 desc=filename, ncols=80, initial=start_byte, position=None) as pbar:
            with open(output_path, 'ab' if resume_file else 'wb') as f:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))

        return True, filename, None
    
    except requests.exceptions.RequestException as e:
        error_msg = str(e)
        return False, filename if 'filename' in locals() else url, error_msg


def download(links_file=None, output_dir="./", max_workers=10, retry_count=3):
    """
    Download multiple files from a list of URLs concurrently with pause/resume support
    
    Args:
        links_file (str): Path to file containing URLs
        output_dir (str): Directory to save downloaded files
        max_workers (int): Number of concurrent downloads
        retry_count (int): Number of retry attempts for failed downloads
    """
    if links_file is None:
        raise LinksFileException()
    
    try:
        with open(links_file, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading links file: {str(e)}")
        return
    
    print(f"Found {len(urls)} URLs to download")
    
    successful = []
    failed = []
    
    os.makedirs(output_dir, exist_ok=True)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {}
        for url in urls:
            # Check for partially downloaded files
            resume_file = os.path.join(output_dir, get_filename_from_url(url))
            if os.path.exists(resume_file):
                print(f"Resuming download for {url}")
            else:
                resume_file = None
            
            futures[executor.submit(download_with_retry, url, output_dir, retry_count, resume_file)] = url
        
        for future in as_completed(futures):
            url = futures[future]
            try:
                success, filename, error = future.result()
                if success:
                    successful.append(filename)
                else:
                    failed.append((url, error))
            except Exception as e:
                failed.append((url, str(e)))
    
    print("\nDownload Summary:")
    print(f"Successfully downloaded: {len(successful)} files")
    if successful:
        print("Successful downloads:")
        for filename in successful:
            print(f"✓ {filename}")
    
    if failed:
        print("\nFailed downloads:")
        for url, error in failed:
            print(f"✗ {url}: {error}")


def download_with_retry(url, output_dir, retry_count, resume_file=None):
    """
    Wrapper function to handle retries for a single download with pause/resume support
    
    Args:
        url (str): URL to download
        output_dir (str): Directory to save downloaded files
        retry_count (int): Number of retry attempts
        resume_file (str): Path to the partially downloaded file (if any)
    
    Returns:
        tuple: (success (bool), filename (str), error message (str) or None)
    """
    for retry in range(retry_count):
        success, filename, error = download_file(url, output_dir, resume_file=resume_file)
        if success:
            return True, filename, None
        
        if retry < retry_count - 1:
            print(f"\nRetrying {url} ({retry+1}/{retry_count})")
            time.sleep(2)  # Wait before retry
    
    return False, url, error


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Download files from a list of URLs")
    parser.add_argument("links_file", help="File containing URLs to download")
    parser.add_argument("--output-dir", "-o", default="./",
                        help="Output directory for downloaded files")
    parser.add_argument("--workers", "-w", type=int, default=10,
                        help="Number of concurrent downloads")
    parser.add_argument("--retries", "-r", type=int, default=3,
                        help="Number of retry attempts for failed downloads")
    
    args = parser.parse_args()
    
    download(args.links_file, args.output_dir, 
             args.workers, args.retries)