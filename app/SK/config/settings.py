from typing import Final

class Settings:
  ## API END - POINTS
  JOB_LISTINGS_URL: Final[str] = 'https://www.sukarne.com/es_mx/retosk_vacantes/';
  APPLICATION_POST_URL: Final[str] = 'https://www.sukarne.com/wp-admin/admin-ajax.php';

 # Default headers
  DEFAULT_HEADERS: Final[dict] = {
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'Accept-encoding': "gzip, deflate, br, zstd",
    'Connection': "keep-alive", 
    }
  
settings = Settings();