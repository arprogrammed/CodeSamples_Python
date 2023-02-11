import justpy as jp

def app():
    wp = jp.QuasarPage()

    h1 = jp.QDiv(a=wp, text='Analysis of Course Reviews', classes='text-h1 text-center q-pa-lg inset-shadow-down shadow-5')
    p1 = jp.QDiv(a=wp, text='These graphs represent a course review analysis.', classes='text-body1 text-center q-pa-md')

    return wp

jp.justpy(app)