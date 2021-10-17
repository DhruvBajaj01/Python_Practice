from tkinter import *
import base64
def display_encode():
    enc = []
    for _ in range(len(main_title_box.get())):
        key_c = key_box.get()[_ % len(key_box.get())]
        enc.append(chr((ord(main_title_box.get()[_]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def display_decode():
    dec = []
    new_message = base64.urlsafe_b64decode(main_title_box.get()).decode()
    for i in range(len(new_message)):
        key_c = key_box.get()[i % len(key_box.get())]
        dec.append(chr((256 + ord(new_message[i])- ord(key_c)) % 256))
    return "".join(dec)


def Mode():
    if(mode_box.get() == 'e'):
        result_box.insert(0,display_encode())
    elif(mode_box.get() == 'd'):
        result_box.insert(0,display_decode())
    else:
        result_box.insert(0,'Invalid Mode')


def reset_message() :
    mode_box.delete(0,"end")
    main_title_box.delete(0,"end")
    key_box.delete(0,"end")
    result_box.delete(0,"end")

def end_process():
    window.destroy()




window = Tk()

window.title("ENCODEDECODE")
window.config(width = 300, height = 250, padx = 100, pady =20)

main_title = Label(text = "ENCODER AND DECODER", font = ("Arial",24))
main_title.grid(column = 0,row =0, columnspan = 2)
main_title_box = Entry( width = 40)
main_title_box.grid(column = 1, row = 1)
message = Label(text = "MESSAGE", font = ("Arial", 18), justify = "left")
message.grid(column = 0, row = 1, pady = 10, padx = 20)
key = Label(text = "KEY", font = ("Arial, 18"),justify = "left")
key_box = Entry( width = 40)
key_box.grid(column = 1, row = 2)
key.grid(column = 0, row = 2, padx = 20 , pady = 10)
mode = Label(text = "MODE (e-encode,d-decode)", font = ("Arial",18),justify = "left")
mode.grid(column = 0, row = 3, padx = 20, pady = 10)
mode_box = Entry(width = 40)
mode_box.grid(column = 1, row = 3)

result = Button(text = "RESULT",width = 20,command = Mode)
result.grid(column = 0, row =4)

result_box = Entry(width = 40)
result_box.grid(column = 1, row = 4)

reset = Button(text = "RESET",width = 20, bg = 'green',command = reset_message )
reset.grid(column = 0, row = 5, pady = 20)

exit = Button(text = "EXIT",width = 20, bg = 'red', command =end_process)
exit.grid(column = 1, row = 5, pady = 20)











window.mainloop()

