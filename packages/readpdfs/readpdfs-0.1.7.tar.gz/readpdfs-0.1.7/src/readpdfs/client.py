import re
import requests
import json
from typing import Optional, Dict, Any, List

class ReadPDFs:
    def __init__(self, api_key: str, base_url: str = "https://backend.readpdfs.com"):
        self.api_key = api_key
        self.base_url = base_url
    def process_pdf(self, 
                    pdf_url: Optional[str] = None, 
                    file_content: Optional[bytes] = None,
                    filename: Optional[str] = None,
                    quality: str = "standard") -> Dict[str, Any]:
        """
        Process a PDF file and convert it to markdown.
        Args:
            pdf_url (str, optional): URL of the PDF file to process.
            file_content (bytes, optional): Raw bytes of the PDF file to upload.
            filename (str, optional): Name of the file when uploading raw bytes.
            quality (str, optional): Quality of processing, either "standard" or "high".
        Returns:
            dict: A dictionary containing the response from the API.
        """
        endpoint = f"{self.base_url}/process_pdf/"
        headers = {
            "x-api-key": self.api_key,
        }
        
        # Validate inputs
        if pdf_url and file_content:
            raise ValueError("Provide either pdf_url or file_content, not both")
        if not pdf_url and not file_content:
            raise ValueError("Either pdf_url or file_content must be provided")
        if file_content and not filename:
            raise ValueError("filename must be provided when using file_content")
            
        if pdf_url:
            # URL-based processing
            data = {
                "pdf_url": pdf_url,
                "quality": quality
            }
            response = requests.post(endpoint, headers=headers, json=data)
        else:
            # File upload processing
            params = {
                'uploadFile': 'True',
                'quality': quality
            }
            
            files = {
                'file': (filename, file_content, 'application/pdf')
            }
            
            response = requests.post(
                endpoint,
                params=params,  # Note: using params instead of data
                headers=headers,
                files=files
            )
            
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}") 
    def process_image(self,
                     image_url: Optional[str] = None,
                     file_content: Optional[bytes] = None,
                     filename: Optional[str] = None,
                     quality: str = "standard") -> Dict[str, Any]:
        """
        Process an image file and convert it to markdown.
        Args:
            image_url (str, optional): URL of the image file to process.
            file_content (bytes, optional): Raw bytes of the image file to upload.
            filename (str, optional): Name of the file when uploading raw bytes.
            quality (str, optional): Quality of processing, either "standard" or "high".
        Returns:
            dict: A dictionary containing the response from the API.
        """
        endpoint = f"{self.base_url}/process-image/"
        headers = {
            "x-api-key": self.api_key,
        }
        
        # Validate inputs
        if image_url and file_content:
            raise ValueError("Provide either image_url or file_content, not both")
        if not image_url and not file_content:
            raise ValueError("Either image_url or file_content must be provided")
        if file_content and not filename:
            raise ValueError("filename must be provided when using file_content")
            
        if image_url:
            # URL-based processing
            data = {
                "image_url": image_url,
                "quality": quality
            }
            response = requests.post(endpoint, headers=headers, json=data)
        else:
            # File upload processing
            params = {
                'uploadFile': 'True',
                'quality': quality
            }
            
            files = {
                'file': (filename, file_content, 'image/jpeg')  # Adjust content-type as needed
            }
            
            response = requests.post(
                endpoint,
                params=params,
                headers=headers,
                files=files
            )
            
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")
    def fetch_markdown(self, url: str) -> str:
        """
        Fetch the markdown content from a given URL.
        Args:
            url (str): URL of the markdown content.
        Returns:
            str: The markdown content.
        """
        endpoint = f"{self.base_url}/fetch_markdown/"
        params = {"url": url}
        response = requests.get(endpoint, params=params)
        
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")

    def process_markdown(self, content: str) -> Dict[int, str]:
        """
        Process markdown content and split it into pages.
        Args:
            content (str): The markdown content to process.
        Returns:
            Dict[int, str]: Dictionary of page numbers and their content.
        """
        if not content:
            raise ValueError("Empty markdown content")

        try:
            pages = re.split(r'<!-- PAGE \d+ -->', content)
            pages = [page.strip() for page in pages if page.strip()]
            page_dict = {i: content for i, content in enumerate(pages, start=1)}

            if not page_dict:
                raise ValueError("No extractable text found in the markdown")

            return page_dict
        except Exception as e:
            raise ValueError(f"Failed to process markdown: {str(e)}")

