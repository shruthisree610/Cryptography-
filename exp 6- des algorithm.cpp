#include <stdio.h>
#include <string.h>

void des_process(char text[], int key)
{
    int i;

    for(i = 0; i < strlen(text); i++)
    {
        text[i] = text[i] ^ key;   // XOR operation
    }
}

int main()
{
    char text[100];
    int key;
    char choice;

    printf("Enter E for Encryption or D for Decryption: ");
    scanf(" %c", &choice);

    printf("Enter the text: ");
    scanf("%s", text);

    printf("Enter the key: ");
    scanf("%d", &key);

    if(choice == 'E' || choice == 'e')
    {
        des_process(text, key);
        printf("Encrypted text: %s\n", text);
    }
    else if(choice == 'D' || choice == 'd')
    {
        des_process(text, key);
        printf("Decrypted text: %s\n", text);
    }
    else
    {
        printf("Invalid choice\n");
    }

    return 0;
}