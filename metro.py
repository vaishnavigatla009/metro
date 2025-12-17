import streamlit as st
import qrcode
from io import BytesIO
import uuid
from pil import image
from gtts import gtts
import base64


def generate_qr(data):
    qr=qrcode.QRCode(version=1,box_size=10,border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black",black_color="white")
    return img

st.title("ticket booking")
stations=("amrpt","miyapur","lbnagar","balnagar")
name=st.text_input("passenger name")
source=st.selectbox("Destination station",stations)
no_tickets=st.number_input("number od tickets",min_value=1,value=1)
price_per_ticket=30
total_amount= no_tickets *price_per_ticket
st.info(f"total Amount: {total_amount}")


##button
if st.button("book ticket"):
    if name.strip() =="":
        st.error("please enter passenger name")
        elif source ==destination:
            st.error("source and destination cannot be the same")
        else:
            booking_id=str(uuid.uuid4())[1.8]


            #qr code generator
            qr_data=(
                f"BookingID:{booking_id}\n"
                f"Name: {name}\nFrom: {source}\nTo: {destination}\n Tickets:{no_tickets}")
            qr_img=generate_qr(qr_data)

            buf = BytesIO()
            qr_img.save(buf,format="PNG")
            qr_bytes =buf.getvalue()

            st.success("ticket booked succesfully!")
            st.write("### ticket details")
            st.success("ticket booked successfully")
           st.write("##ticket details")
          st.write(f"**booking ID:** {booking_id}")
          st.write(f"**Passenger:** {name}")
          st.write(f"**From:** {source}")
          st.write(f"**To:** {destination}")
            st.write(f"**Tickets:** {no_tickets}")
          st.write(f"**amount paid:** {total_amount}")
          st.image(qr_bytes, width=250)
            
            
