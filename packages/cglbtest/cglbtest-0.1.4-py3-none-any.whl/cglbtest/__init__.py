from.file_reader_manager import FileReaderManager
from.file_reader_txt import FileReaderTxt
from.file_reader_csv import FileReaderCsv
GLOBAL_FILE_READER_MANAGER=FileReaderManager()
GLOBAL_FILE_READER_MANAGER.add(FileReaderTxt,['txt'])
GLOBAL_FILE_READER_MANAGER.add(FileReaderCsv,['csv'])
from.file_reader_img import FileReaderImg
GLOBAL_FILE_READER_MANAGER.add(FileReaderImg,['png','jpg','jpeg','gif','bmp','tiff','tif'])
from cglbtest.file_reader_nc import FileReaderNc
GLOBAL_FILE_READER_MANAGER.add(FileReaderNc,['.nc'])