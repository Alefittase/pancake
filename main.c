#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    while(1)
    {
    int guess;
    int ans;
    int a=0,b=0,c=0,d=0,e=0,f=0;
    printf("\n");
    srand(time(NULL));
    int board[64];
    for (int i=0;i<64;i++)
    {
        board[i] = rand()%2;
    }
    for (int i=1;i<64;i+=2)
    {
        a+=board[i];
    }
    (a%2==0)?(a=1):(a=0);
    for(int k=2;k<4;k++)
    {
        for (int i=k;i<64;i+=4)
        {
            b+=board[i];
        }
    }
    (b%2==0)?(b=1):(b=0);
    for(int k=4;k<8;k++)
    {
        for (int i=k;i<64;i+=8)
        {
            c+=board[i];
        }
    }
    (c%2==0)?(c=1):(c=0);
    for (int k=8;k<64;k+=16)
    {
        for (int i=k;i<k+8;i+=1)
        {
            d+=board[i];
        }
    }
    (d%2==0)?(d=1):(d=0);
    for (int k=16;k<64;k+=32)
    {
        for (int i=k;i<k+16;i+=1)
        {
            e+=board[i];
        }
    }
    (e%2==0)?(e=1):(e=0);
    for (int i=32;i<64;i+=1)
    {
        f+=board[i];
    }
    (f%2==0)?(f=1):(f=0);
    for (int i=0;i<64;i++)
    {
        printf("%d ",board[i]);
        if(i%8==7 && i!=0)
        {
            printf("\n");
        }
    }
    ans = f+2*e+4*d+8*c+16*b+32*a;
    printf("\n");
    printf("Guess: ");
    scanf("%d",&guess);
    if (guess == ans)
    {
        printf("YOU WON!\n");
    }
    else
    {
        printf("YOU LOST!");
    }
    }
    
}
