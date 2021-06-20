

def mail():
    import smtplib
    sender_email = "sender_email here"
    receiver_email = "receiver_email here"
    password = ("your password here")
    message = "Hello this was sent by using Python"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email,password)
    print("Login Success")
    server.sendmail(sender_email,receiver_email,message)
    print("Email has been seen to ", receiver_email)

def whatsapp():
    import pywhatkit
    pywhatkit.sendwhatmsg_instantly("receiver_phone_no" , 'One face has been recognised')
    print("Whatsapp message has been sent")

def launch_ec2():
    import os
    os.system("aws ec2 run-instances  --image-id  ami-0ad704c126371a549  --instance-type t2.micro --key-name new_aws  --security-group-ids sg-f9e80b85 --subnet-id subnet-39748152 --count 1")

def creating_EBS_volume():
    import os
    os.system("aws ec2 create-volume --availability-zone ap-south-1a --size 5 --volume-type gp2")