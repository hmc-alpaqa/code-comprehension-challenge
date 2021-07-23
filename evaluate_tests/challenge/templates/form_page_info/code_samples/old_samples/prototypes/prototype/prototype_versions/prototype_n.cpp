#include <string.h>
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <limits.h>


struct MysteryStruct {
  int str_index;
  int str_len;
  int special_val;
  int special_product;
  char* str;
};

//Shown
MysteryStruct* func0(int input);
void func1(int input1[], int input2, int input3);
int func2(int input1, int input2);
void func3(MysteryStruct* mystery_struct, int input1[],
			       int input2);
void func4(MysteryStruct* mystery_struct, int input1);

//Hidden
MysteryStruct* initialize_MysteryStruct();
void func5(MysteryStruct* mystery_struct);
void func6(MysteryStruct* mystery_struct);
void func7(MysteryStruct* mystery_struct);
void add_letter(MysteryStruct* mystery_struct, char letter);
int parse_input(char* input, int* value);
void read_input_file(FILE* file, int** tests, int* num_tests, int* invalid_test);

MysteryStruct* initialize_MysteryStruct() {
  MysteryStruct* mystery_struct = (MysteryStruct*) malloc(sizeof(MysteryStruct));
  mystery_struct->str_index = 0;
  mystery_struct->str_len = 2;
  mystery_struct->str = (char*) calloc(3, sizeof(char));
  mystery_struct->str[2] = '\0';
  mystery_struct->special_val = 0;
  mystery_struct->special_product = 1;
  return mystery_struct;
}

void func5(MysteryStruct* mystery_struct) {
  add_letter(mystery_struct, '1');
  mystery_struct->special_val += (1 * mystery_struct->special_product);
  mystery_struct->special_product++;
}
void func6(MysteryStruct* mystery_struct) {
  add_letter(mystery_struct, '2');
  mystery_struct->special_val += (64 * mystery_struct->special_product);
  mystery_struct->special_product++;
}
void func7(MysteryStruct* mystery_struct) {
  add_letter(mystery_struct, '3');
  mystery_struct->special_val += (4096 * mystery_struct->special_product);
  mystery_struct->special_product++;
}

void add_letter(MysteryStruct* mystery_struct, char letter) {
  int index = mystery_struct->str_index % mystery_struct->str_len;
  mystery_struct->str[index] = letter;
  mystery_struct->str_index++;
}
  

//start
MysteryStruct* func0(int input) {
  int var1 = 4;
  int var2[var1];

  func1(var2, var1, input);

  MysteryStruct* mystery_struct = initialize_MysteryStruct();
  func3(mystery_struct, var2, var1);

  return mystery_struct;
}

void func1(int input1[], int input2, int input3) {
  int var1 = 8;
  
  for(int i = 0; i < input2; i++) {
    int var2 = func2(input3, var1);

    
    input3 = input3 / var1;
    
    input1[i] = var2;
  }
}

int func2(int input1, int input2) {
  int var1;
  int var2 = input1 % input2;

  if(var2 < (input2 - 3)) {
    var1 = 0;
    
  } else if(var2 > (input2 - 3)) {
    var1 = 1;
    
  } else {
    var1 = 2;
  }

  return var1;
}

void func3(MysteryStruct* mystery_struct, int input1[],
			      int input2) {
  
  for(int i = 0; i < (input2 - 1); i+=2) {
    int var1 = input1[i] + input1[i + 1];
    
    func4(mystery_struct, var1);
  }
}

void func4(MysteryStruct* mystery_struct, int input1) {
  if(input1 < 2) {
    func5(mystery_struct);
    
  } else if(input1 == 2) {
    func6(mystery_struct);
    
  } else {
    func7(mystery_struct);
  }
}
//end

//Points value to the number represented by input.
//Returns 0 on success and -1 on invalid input.
int parse_input(char* input, int* value) {
  if(strlen(input) == 0) {
    return -1;
  }

  char* endptr;
  int parse_res;
  long strtol_res = strtol(input, &endptr, 10);
  
  if(strlen(endptr) == 0 || (strlen(endptr) == 1 && endptr[0] == '\n')) {
    if(strtol_res > INT_MAX || strtol_res < INT_MIN) {
      parse_res = -1;

    } else {
      *value = (int) strtol_res;
      parse_res = 0;
    }
    
  } else {
    parse_res = 1;
  }

  return parse_res;
}

void read_input_file(FILE* file, int** tests, int* num_tests, int* invalid_test) {
  int max_line_length = 100;
  int max_inputs = 4096;
  char line[max_line_length];

  *tests = (int*) malloc(max_inputs * sizeof(int));
  *num_tests = 0;
  *invalid_test = 0;
  
  while(fgets(line, max_line_length, file)) {
    int value;
    int parse_res = parse_input(line, &value);

    if(parse_res == 0) {
      (*tests)[(*num_tests)++] = value;
    } else {
      *invalid_test = 1;
    }
  }
}

int main(int argc, char* argv[]) {
  /*char* filename = argv[1];
  FILE* file = fopen(filename, "r");
  int* tests;
  int num_tests;
  int invalid_test;
  read_input_file(file, &tests, &num_tests, &invalid_test);
  if(invalid_test) {
    printf("At least one test was invalid\n");
  }

  for(int i = 0; i < num_tests; i++) {
    MysteryStruct* result = func0(tests[i]);
    free(result);
    }*/

  return 0;
}
