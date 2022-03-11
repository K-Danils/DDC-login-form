# DDC-login-form

Instrukcijas lai palaistu lokāli. (nepieciešams Python un Pip)

1. Lejupielādēt / klonēt resursu failus, tad terminālī ievadīt:  
    cd ...jūsu path\DDC-login-form-main  

2. nepieciešams instalēt visas paciņas norādītas requirements.txt  
    pip install -r requirements.txt  

3. Jānokļūst project mapē ar:  
    cd project  

4. tad priekš bash:  
    export FLASK_APP=main  
    flask run  
    
    priekš Fish  
    set -x FLASK_APP main  
    flask run  

    priekš CMD  
    set FLASK_APP=main  
    flask run  

    priekš Powershell  
     $env:FLASK_APP = "main"  
     flask run  

5. tagad projektam ir jābūt pieejamam http://127.0.0.1:5000/

Datu bāzē jau ir pāris ieraksti, lai demonstrētu mājaslapas darbību.  
testa konta login info:   
    phone: +37123456789 vai 23456789  
    password: Password1!  
