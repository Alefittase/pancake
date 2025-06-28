#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int board[64], guess, ans, parity[6];
int main(){
    srand(time(NULL));
    for(int i=0; i<64; i++){
        board[i]=rand()&1;
        if(0==i%2) parity[0]+=board[i];
        if(2<=i%4) parity[1]+=board[i];
        if(4<=i%8) parity[2]+=board[i];
        if(8<=i%16) parity[3]+=board[i];
        if(16<=i%32) parity[4]+=board[i];
        if(32<=i%64) parity[5]+=board[i];
    }
    int k=32;
    for(int i=0; i<6; i++){
        if(!(parity[i]&1)) ans+=k;
        k/=2;
    }
    for(int i=0; i<64; i++){
        printf("%d ",board[i]);
        if(i%8==7) printf("\n");
    }
    printf("\nGuess: ");
    scanf("%d", &guess);
    if(guess==ans) printf("YOU WON!\n");
    else printf("YOU LOST!\nThe answer is %d\n", ans);
    return 0;
}