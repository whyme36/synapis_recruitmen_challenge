
import re


# function turns the splited text into paragraphs not exceeding the given number of characters
def creating_tuples_of_paragraph(array_splited_text, maximum_width,table_of_justify):
    count=0
    row = ''
    for index,word in enumerate(array_splited_text): #it's take every word whit index
        if count+len(word)<=maximum_width: #check if word will fit
            count+=len(word)+1
            row+=word+' '
        else: #if not, take rest of the words form array_splited_text, and do function again
            creating_tuples_of_paragraph(array_splited_text[index:],maximum_width,table_of_justify)
            break

    row=row[:-1]
    table_of_justify.append(row) # add word to array, whitout last space

# function fits a string to the specified length by adding spaces between words starting from the left
def add_space_from_left(String,maximum_width):
    #calculate how much spaces needed to compensate for the length, and how many spaces string has
    number_of_spaces_needed = maximum_width - len(String)
    how_many_spaces = len(String.split(' ')) - 1
    output = ''
    if number_of_spaces_needed <= how_many_spaces and number_of_spaces_needed!=0: #if number_of_spaces_needed is smaler then spaces in string and it's not 0
        String_splited = String.split(' ', number_of_spaces_needed) #split string form the right into number_of_spaces_needed pieces
        output = "  ".join(String_splited) #and add betwen that pieces extra speces
    elif how_many_spaces==0 or number_of_spaces_needed==0:
        output=String #get back string
    else: # when number of number_of_spaces_needed is bigger than number of spaces in string
        spaces_count=int(number_of_spaces_needed/how_many_spaces) # find the number of spaces you can fit into each word gap and create string whit that amount
        i=0
        spaces=''
        while i<=spaces_count:
            spaces+=' '
            i+=1
        String_splited = String.split(' ') #
        output = spaces.join(String_splited)
        output=add_space_from_left(output,maximum_width)# to fit the rest needed spaces, function need go back to itselft

    return output

#function converts the cut String into justify text
def justify_text(splited_text,maximum_width,table_of_justify):
    creating_tuples_of_paragraph(splited_text, maximum_width,table_of_justify)
    jtable_of_justify = table_of_justify[::-1]
    print('[')
    for i in jtable_of_justify:
        print(f'\t"{add_space_from_left(i, maximum_width)}"')
    print(']')

if __name__ == "__main__":
    text = input() #"Hey there mate, it’s nice to finally meet you"
    maximum_width = int(input())#16
    table_of_justify = []
    splited_text = re.split(' ', text)
    justify_text(splited_text,maximum_width,table_of_justify)


