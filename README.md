# dash-template
A Template for Dash Web Application, Author: [Young](mailto:wzyjsha@163.com)

# Environment
- python version: 3.7.13
- conda environment: [dash-template.yaml](dash-template.yaml)  

# File Structure
```python
dash-template
│
├─project  
│   ├─assets  
│   │  ├─background  
│   │  ├─icon  
│   │  ├─illustration  
│   │  └─logo  
│   ├─config  
│   ├─site_component  
│   └─src  
├─.gitignore
├─dash-template.yaml
├─LICENSE
├─README.md
└─requiremnets.txt
```

# Setup
```python
pip install requirements.txt
cd project
python manage.py
```
- The main file is [manage.py](project/manage.py), when add the new site page, you need to add the **app servrr** into the mounts of the [manage.py](project/manage.py).


# Related Resources
- Theme: [Flatly](https://bootswatch.com/flatly/), and **bootstrap.min.css** file can be seen in this [Web Link](https://bootswatch.com/5/flatly/bootstrap.min.css).
- The [background-picture](project/assets/background/pexels-prakash-aryal-38326.jpg) in the Home site is from [Pexels](https://images.pexels.com/photos/38326/pexels-photo-38326.jpeg?auto=compress&cs=tinysrgb&w=600).
- The icons are from [Font Awesome](https://fontawesome.com/icons).