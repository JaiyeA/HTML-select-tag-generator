import tkinter
import Parameters

params = Parameters.parameters()

def generator(options_text):
    generated_html = ''
    character_split = ''
    option_array = []
    for char in options_text:
        if char != '\n':
            character_split = character_split + char
        else:
            option_array.append(character_split)
            character_split = ''
    generated_html = '<select'
    if params.get_class() != '':
        generated_html = generated_html +' class="'+params.get_class()+'"'
    if params.get_name() != '':
        generated_html = generated_html +' name="'+params.get_name()+'"'
    if params.get_id() != '':
        generated_html = generated_html +' id="'+params.get_id()+'"'
    if params.get_size() != '':
        generated_html = generated_html +' size='+params.get_size()
    generated_html = generated_html +'>\n'
    for option in option_array:
        option_tag = '  <option value="'+option+'">'+option+'</option>\n'
        generated_html = generated_html + option_tag
    return generated_html + '</select>'

def main():
    window = tkinter.Tk()
    window.title('HTML Generator')
    top_frame = tkinter.Frame(window)

    label2 =tkinter.Label(top_frame, text='*Select Option Dropdown only*\n\nWhat is the class name of the dropdown? (optional)')
    entry2_id = tkinter.StringVar()
    entry2 = tkinter.Entry(top_frame, textvariable=entry2_id)

    label3 =tkinter.Label(top_frame, text='What is the name of the dropdown? (optional)')
    entry3_id = tkinter.StringVar()
    entry3 = tkinter.Entry(top_frame, textvariable=entry3_id)

    label4 =tkinter.Label(top_frame, text='What is the id of the dropdown? (optional)')
    entry4_id = tkinter.StringVar()
    entry4 = tkinter.Entry(top_frame, textvariable=entry4_id)

    label5 =tkinter.Label(top_frame, text='What is the size of the dropdown? (optional)')
    entry5_id = tkinter.StringVar()
    entry5 = tkinter.Entry(top_frame,textvariable=entry5_id)

    label6 = tkinter.Label(top_frame,text='Enter your list of options\n(Important: List the options under one another in multi-line format.)')
    text_box = tkinter.Text(top_frame, height=5, width=75, borderwidth=2, relief='groove')

    result_label = tkinter.Label(top_frame, text='Generated Code\n(Copy and paste this into your HTML file)')
    Result_text_box = tkinter.Text(top_frame, height=20, width=75, borderwidth=2, relief='groove')

    Back_button = tkinter.Button(top_frame, text='Back', command=lambda: [Result_text_box.pack_forget(),
    Back_button.pack_forget(),Reset_button.pack_forget(),label2.pack(),Result_text_box.delete('1.0',tkinter.END),
    entry2.pack(),label3.pack(),entry3.pack(),label4.pack(),entry4.pack(),label5.pack(),
    entry5.pack(),label6.pack(),text_box.pack(),generate_button.pack()])

    Reset_button = tkinter.Button(top_frame, text='Reset', command=lambda: [window.destroy(),main()])

    generate_button = tkinter.Button(top_frame, text='Generate', command= lambda: [params.set_class(entry2.get()),
        params.set_name(entry3.get()),params.set_id(entry4.get()),params.set_size(entry5.get()),
        label2.pack_forget(),label3.pack_forget(),label4.pack_forget(),label5.pack_forget(),
        label6.pack_forget(),entry2.pack_forget(),entry3.pack_forget(),result_label.pack(),
        entry4.pack_forget(),entry5.pack_forget(),text_box.pack_forget(),Result_text_box.pack(),
        Back_button.pack(side = tkinter.LEFT, fill='none', expand=True),
        Reset_button.pack(side = tkinter.LEFT, fill='none', expand=True),generate_button.pack_forget(),
        Result_text_box.insert('1.0',generator(text_box.get('1.0','end-1c')+'\n'))])

    label2.pack()
    entry2.pack()

    label3.pack()
    entry3.pack()

    label4.pack()
    entry4.pack()

    label5.pack()
    entry5.pack()

    label6.pack()
    text_box.pack()

    generate_button.pack()
    top_frame.pack()
    window.mainloop()
main()
