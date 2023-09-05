#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

/**
 * Keys:
 * 4 - 32 bit
 * 3 - 1 bit
 * total 4 * 32 + 3 bits
 * 131 bits keys to be found
 * So there can be 2^131 combinations
 * 
 * 7 keys
 * 11 unknowns
*/


void arf(int i1, int i2, int i3, int i4, int i5, 
         int G1, int G2, 
         int GG1, int GG2, 
         int key1, int key2, int key3, int key4, bool key5, bool key6, bool key7)
{
   int op1, op2, op3, op4, op5, op6, op7, op8;
   int op9, op10, op11, op12, op13, op14, op15, op16;
   int op17, op18, op19, op20, op21, op22, op23, op24;
   int op25, op26, op27, op28;
   int o1, o2, o3, o4;

   op1 = GG1 * i1;
   op2 = GG2 * i2;
   op3 = G1 * i2;
   op4 = G2 * i1;
   if (G1 > 10)
   {
      op5 = (G1 * i3) + GG1;
      op6 = op5 - (G2 * i1);
   }
   else
   {
      op5 = i3 * i4;
      op6 = op5 - (G1 * i2);
   }

   if (!((op5 < (G2 * i1)) ^ key7))
   {
      op6 = (G2 * i4) - i3;
      op17 = op6 - G2;
   }
   else
   {
      op17 = op2 - op4;
      op2 = op4 - op17;
      op17 = op17 - op2;
   }
   op7 = G1 * i4;
   op8 = G2 * i3;

   op9 = op1 + op2;
   op10 = op3 + op4;
   op11 = op4 + op6;
   op12 = op7 + op8;

   op13 = op11 + G1;
   o1 = op13 + key1;
   op14 = i5 + op12;
   o2 = op14 + key2;
   op15 = G1 * op14;
   op16 = op13 * G2;

   if (op13 == op14)
   {
      op17 = op17 * op11;
      op14 = op14 - op17;
      op15 = op15 + op17;
   }
   else
      op14 = op13 * G1;
   
   op18 = op14 * G2;
   op19 = op15 * op16;
   op20 = op17 + op18;
   op21 = G1 * op20;
   op22 = op19 * G2;
   op23 = op19 * G1;
   op24 = key5 ? op20 + G1 : op20 * G2;
   op25 = op21 + op22;
   op26 = key6 ? op23 + op24 : op23 - 1;
   op27 = op9 + op25 / key3;
   o3 = op27;
   op28 = op10 + op26;
   o4 = op28 + key4;

   printf("%d\n", o1);
   printf("%d\n", o2);
   printf("%d\n", o3);
   printf("%d\n", o4);
}

int main()
{
   // for (int i = 0; i < 11; i++) {
   //    printf("Random no: %d %d\n", i, rand() % 200);
   // }
   arf(5, -1, -1, 1, -2, -2, 1, 3, -1, -89, 1243, 7, -9, false, true, true);
   return 0;
}


/**
 

g2*i1 +
If((g2*i1 <= If(g1 <= 10, i3*i4, g1*i3 + gg1)) == k7,
   If(g1 <= 10,
      If(g1 <= 10, i3*i4, g1*i3 + gg1) + -1*g1*i2,
      If(g1 <= 10, i3*i4, g1*i3 + gg1) + -1*g2*i1),
   g2*i4 + -1*i3) +
g1 +
k1


*/