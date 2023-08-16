#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
    long size;
    unsigned char *string;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    string = (unsigned char *)((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", (char *)string);
    printf("  first %ld bytes:", size < 10 ? size : 10);

    for (long i = 0; i < (size < 10 ? size : 10); i++)
    {
        printf(" %02x", string[i]);
    }

    printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
    long size;
    PyObject *obj;
    PyObject *item;

    size = ((PyVarObject *)p)->ob_size;
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);

    for (long i = 0; i < size; i++)
    {
        obj = ((PyListObject *)p)->ob_item[i];
        printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);

        if (obj->ob_type == &PyBytes_Type)
        {
            item = obj;
            print_python_bytes(item);
        }
    }
}
