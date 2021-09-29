
import streamlit as st  
import random as _random
import string 



#Take a look at your chrome tab. With the code below you can change the header of the page
st.set_page_config(
        page_title='Mnemo Password Generator',
        page_icon="🔑"
        )



#Display a GIF on top of the app
st.markdown("![Alt Text](https://media.giphy.com/media/GbCDfM8ZaLaHo4F9Vf/giphy.gif?cid=790b7611452765a1af28cc3489d67553872f96a3af0ed7c0&rid=giphy.gif&ct=g)")


#Title of your app + one whitespace
st.markdown("<h1 style='text-align: center; color: black;'>Mnemo password generator </h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)


length = st.number_input('How many characters do you want your password to have? (10-100)', min_value=10, max_value=100)

#st.write('The current number is ', number)
st.markdown("<h5 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)


title = st.write('What should your password include?')

st.markdown("<h5 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)

cb1 = st.checkbox('Numbers')
cb2 = st.checkbox('Letters')
cb3 = st.checkbox('Special Characters ($%?!)')


empty = st.empty()



if cb1 == True:
        numbers = "0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"
else:
        numbers = ""


if cb2 == True:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
else:
        letters = ""


if cb3 == True:
        symbols = string.punctuation
else:
        symbols = ""


if cb1 and cb1 and cb3 == None: 
        st.write("Check")


all = letters + str(numbers) + symbols

try:
        temp = _random.sample(all, length)
except ValueError:
        pass
                
try:
        temp2 = _random.sample(all, length)
except ValueError:
        pass

try:
        temp3 = _random.sample(all, length)
except ValueError:
        pass

try:
        temp4 = _random.sample(all, length)
except ValueError:
        pass



try:
        password = "".join(temp)
except ValueError and NameError:
        pass

try:
        password2 = "".join(temp2)
except ValueError and NameError:
        pass

try:
        password3 = "".join(temp3)
except ValueError and NameError:
        pass

try:
        password4 = "".join(temp4)
except ValueError and NameError:
        pass






st.markdown("<h5 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)
try: 
        title2 = st.write(' ')
except:
        NameError
        st.write(" ")
st.markdown("<h5 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)

try:
        st.code(password)
        st.code(password2)
        st.code(password3)
        st.code(password4)

except ValueError and NameError:
        st.write("Select a box")       
















#i used these lines for additional whitespace between the result and the text boxes
st.markdown("<h5 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)






#whitespace again
st.markdown("<h3 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)






#instagram link
link = '[Just a tiny example app for my Instagram post](https://www.instagram.com/max_mnemo)'
st.markdown(link, unsafe_allow_html=True)


