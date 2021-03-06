# ---------- INSTALL DJANGO ON MAC ----------
 
1. Check your Python version by typing in the terminal : python --version
 
2. You want Python 3.4 or higher. Type the following to see if you have Python 3 in the terminal : python3 --version
 
3. If you need Python 3.4 or above do this
 
	A. Download Python at https://www.python.org/downloads
	
	B. Click Download Python 3.5.1 or later
	
	C. Click Open
	
	D. Click continue a few times. Agree to the terms and install. You may have to enter your password.
	
4. Check to see if you have pip installed in the terminal type : pip --version
 
5. If you don't have pip 8 or above type in the terminal : sudo easy_install pip
 
6. Type in the terminal : sudo pip install Django
 
7. Test that Django is installed in the terminal
 
	A. python3
	
	B. import django
	
	C. django.get_version()
	
	D. You should see '1.10.2' or higher
	
8. Create a sample site : django-admin startproject sampsite
 
	A. sampsite is were your project lives
	
		i. __init__.py tells Python that this is a Python package
		
		ii. settings.py has settings for the Django project
		
		iii. urls.py a sort of table of contents for your project
		
		iv. wsgi.py serves your project
	
	B. manage.py allows you to interact with your project
	
9. Start the server : python manage.py runserver
 
# ---------- INSTALL DJANGO ON WINDOWS ----------
 
1. Check your Python version by typing in the terminal : python --version 
(You want Python 3.4 or higher)
 
2. If Python 3.4 or higher isn't installed
 
	A. Go to https://www.python.org/getit/windows/
	
	B. Click on Latest Python 3 Release 
	
	C. Click on Windows x86 executable installer
	
	D. Click Run
	
	E. Check Install for all users and add Python 3 to path
	
		a. Open Control Panel -> System & Security -> System -> Advanced System Settings on the left
		
		b. Environment Variable button
		
		c. Select PATH and click edit
		
		d. Add c:\Pyhon34, or what ever your Python directory is
		
3. Install Pip in the command line type : python -m pip install -U pip
 
4. Create a Python Virtual Environment so we don't have to worry about changing dependencies that your system may not want edited. 
 
	A. Type in Command Prompt : pip install virtualenv
	
	B. Create the virtual environment for your site in command prompt : virtualenv env_site1 
	
	C. Activate the environment in CP 
	
		i. cd Scripts
		
		ii. activate
		
5. Install Django in CP : pip install django
 
6. Test that it works
 
	A. python
	
	B. import django
	
	C. django.get_version()
	
	D. You should see '1.10.2' or higher
	
7. Create a sample site : django-admin startproject sampsite
 
	A. sampsite is were your project lives
	
		i. __init__.py tells Python that this is a Python package
		
		ii. settings.py has settings for the Django project
		
		iii. urls.py a sort of table of contents for your project
		
		iv. wsgi.py serves your project
	
	B. manage.py allows you to interact with your project
	
8. Start the server : python manage.py runserver