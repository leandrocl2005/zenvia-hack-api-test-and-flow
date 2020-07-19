call C:\Users\%USERNAME%\Anaconda3\Scripts\activate.bat C:\Users\%USERNAME%\Anaconda3 


set SECRET_KEY='f1ec162ebde24b6c949dbbd999702459'

call set FLASK_APP=app
call set FLASK_ENV=Development
call set FLASK_DEBUG=True

call "%PROGRAMFILES%\Mozilla Firefox\firefox.exe" http://localhost:8040/

call python -m flask run -p 8040 -h localhost


rem flask db init
rem flask db migrate
rem flask db upgrade

rem flask db revision --autogenerate 
rem flask db upgrade
