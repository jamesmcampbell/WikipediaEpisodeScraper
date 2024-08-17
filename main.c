#include <Python.h>
#include <stdio.h>

//#include "mkvinfo/mkvinfo.cpp"
// #include "fileNames.h"

int main() {
    make_episodes_list_file: 
    {
        Py_Initialize();
        PyRun_SimpleString("exec(open('scrape_h2_h3_table.py').read())");
        Py_Finalize();
    }
    
    print_file_contents: 
    {
        FILE *ep_names = fopen("headers_and_tables.txt", "r");
        if (ep_names == NULL) { printf("Could not open file\n"); return 1; }
        char line[1024];
        while (fgets(line, sizeof(line), ep_names)) 
        {
            if (strncmp(line, "h2: ", 4) == 0) { printf("\n%s", line + 4); }
            if (strncmp(line, "h3: ", 4) == 0) { printf("\n%s", line + 4); }
            if (strncmp(line, "table: ", 7) == 0) { printf("-%s", line + 7); }
        }
    }

    return 0;
}
