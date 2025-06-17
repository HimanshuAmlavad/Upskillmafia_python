try:
    
    user_input = input("Enter text to write to file: ")
    with open('output.txt', 'w') as file:
        file.write(user_input + '\n')
    print("Data successfully written to output.txt \n")
   

   
    additional_input = input("Enter additional text to append: ")
    with open('output.txt', 'a') as file:
        file.write(additional_input + '\n')
    print("Data successfully append.")

    # Read and display final content
    print("\nFinal content of output.txt:")
    print("-" * 30)
    with open('output.txt', 'r') as file:
        content = file.read()
        print(content)

except IOError as e:
    print(f"Error handling file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")