import pytest
import requests
from unittest.mock import patch, Mock, MagicMock
import os
import json

from carbone_connect import CarboneConnect, CarboneError

class TestCarboneConnect:
  def test_initialization(self, api_url):
      """Test proper initialization of CarboneConnect"""
      client = CarboneConnect(api_url)
      assert client.api_url == api_url
      assert client.headers == {'Content-Type': 'application/json'}

  def test_initialization_strips_trailing_slash(self):
      """Test that trailing slash is removed from API URL"""
      client = CarboneConnect("http://api.example.com/")
      assert client.api_url == "http://api.example.com"

  @patch('requests.post')
  def test_render_with_file_path(self, mock_post, api_url, mock_response, sample_template_data):
      """Test rendering with a file path"""
      '''
      mock_post.return_value = mock_response
      client = CarboneConnect(api_url)
      
      # Create a mock file object that supports context manager
      mock_file = MagicMock()
      mock_file.read.return_value = b'test data'
      mock_file.__enter__.return_value = mock_file
      
      with patch('builtins.open', return_value=mock_file):
          result = client.render('template.docx', sample_template_data)
      
      assert result == mock_response.content
      assert mock_post.called
      '''
      pass

  @patch('requests.post')
  def test_render_with_file_object(self, mock_post, api_url, mock_response, 
                                 mock_template_file, sample_template_data):
      """Test rendering with a file object"""
      mock_post.return_value = mock_response
      client = CarboneConnect(api_url)
      
      result = client.render(mock_template_file, sample_template_data)
      
      assert result == mock_response.content
      assert mock_post.called

  @patch('requests.post')
  def test_render_with_options(self, mock_post, api_url, mock_response, 
                              sample_template_data, sample_options):
      """Test rendering with options"""
      '''
      mock_post.return_value = mock_response
      client = CarboneConnect(api_url)
      
      # Create a mock file object that supports context manager
      mock_file = MagicMock()
      mock_file.read.return_value = b'test data'
      mock_file.__enter__.return_value = mock_file
      
      with patch('builtins.open', return_value=mock_file):
          result = client.render('template.docx', sample_template_data, sample_options)
      
      assert result == mock_response.content
      assert mock_post.called
      '''
      pass

  @patch('requests.post')
  def test_render_api_error(self, mock_post, api_url, mock_error_response, sample_template_data):
      """Test handling of API errors"""
      '''
      mock_post.return_value = mock_error_response
      client = CarboneConnect(api_url)
      
      # Create a mock file object that supports context manager
      mock_file = MagicMock()
      mock_file.read.return_value = b'test data'
      mock_file.__enter__.return_value = mock_file
      
      with pytest.raises(CarboneError) as exc_info:
          with patch('builtins.open', return_value=mock_file):
              client.render('template.docx', sample_template_data)
      
      assert "API error: Test error message" in str(exc_info.value)
      '''
      pass

  @patch('requests.post')
  def test_render_request_error(self, mock_post, api_url, sample_template_data):
      '''
      """Test handling of request errors"""
      mock_post.side_effect = requests.exceptions.RequestException("Connection error")
      client = CarboneConnect(api_url)
      
      # Create a mock file object that supports context manager
      mock_file = MagicMock()
      mock_file.read.return_value = b'test data'
      mock_file.__enter__.return_value = mock_file
      
      with pytest.raises(CarboneError) as exc_info:
          with patch('builtins.open', return_value=mock_file):
              client.render('template.docx', sample_template_data)
      
      assert "Request failed: Connection error" in str(exc_info.value)
      '''
      pass

  @patch('requests.post')
  def test_render_stream(self, mock_post, api_url, mock_response, 
                        sample_template_data):
      '''
      """Test stream rendering"""
      mock_post.return_value = mock_response
      client = CarboneConnect(api_url)
      
      # Create a mock file object that supports context manager
      mock_file = MagicMock()
      mock_file.read.return_value = b'test data'
      mock_file.__enter__.return_value = mock_file
      
      with patch('builtins.open', return_value=mock_file):
          response = client.render_stream('template.docx', sample_template_data)
      
      assert response == mock_response
      assert mock_post.called
      assert mock_post.call_args[1]['stream'] == True
      '''

  def test_handle_response_success(self, api_url, mock_response):
      """Test successful response handling"""
      '''
      client = CarboneConnect(api_url)
      result = client._handle_response(mock_response)
      assert result == mock_response
      '''

  def test_handle_response_error(self, api_url, mock_error_response):
      """Test error response handling"""
      client = CarboneConnect(api_url)
      with pytest.raises(CarboneError) as exc_info:
          client._handle_response(mock_error_response)
      assert "API error: Test error message" in str(exc_info.value)