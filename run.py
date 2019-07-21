'''
Created on 17 Jul 2019

@author: Aruna
'''
from FlaskBlog import create_app
app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
