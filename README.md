# DDC-login-form  

Instrukcijas lai palaistu lokāli. (nepieciešams Python un Pip)  

1. Lejupielādēt / klonēt resursu failus, tad terminālī ievadīt:  
    cd <jūsu path>/DDC-login-form-main  

2. Jāizveido virtual environment:   
    Windows    
    py -m venv venv  
      
    MacOS/Linux  
    python3 -m venv venv  

3. Jāaktivizē virtual environment:  
    Windows  
    venv\Scripts\activate  
    
    MacOS/Linux  
    . venv/bin/activate  
    
4. nepieciešams instalēt visas paciņas norādītas requirements.txt  
    pip install -r requirements.txt  

5. Jānokļūst project mapē ar:  
    cd project  

6. tad ir jāpalaiž pats flask projekts:
    Bash    
    export FLASK_APP=main  
    flask run  
    
    Fish  
    set -x FLASK_APP main  
    flask run  

    CMD  
    set FLASK_APP=main  
    flask run  

     Powershell  
     $env:FLASK_APP = "main"  
     flask run  

7. tagad projektam ir jābūt pieejamam http://127.0.0.1:5000/

Datu bāzē jau ir pāris ieraksti, lai demonstrētu mājaslapas darbību.  
testa konta login info:   
    phone: +37123456789 vai 23456789  
    password: Password1!  
