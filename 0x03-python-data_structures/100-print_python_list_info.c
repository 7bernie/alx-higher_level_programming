<<<<<<< HEAD
#include <stdlib.h>
#include <stdio.h>
#include <python.h>
=======
nclude <stdio.h>
#include <Python.h>
>>>>>>> f32d3b9cc935d328965e2ea8a14dc147979603e5

/**
 * print_python_list_info - print info about a Python list.
 * @p: pointer to a list object
 *
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
Py_ssize_t idx = 0;
PyObject *item = NULL;

printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
for (; idx < PyList_Size(p); idx++)
{
	item = PyList_GetItem(p, idx);
	printf("Element %ld: %s\n", idx, item->ob_type->tp_name);
}
}

/**
 * main - Entry point
 *
 * Return: 0 on success, 1 on failure.
 */
int main(void)
{
Py_Initialize();
/* Example list creation */
PyObject *pList = PyList_New(3);
PyObject *pValue;

if (pList == NULL)
{
	PyErr_Print();
	return (1);
}

/* Append objects to the list */
pValue = PyLong_FromLong(1);
PyList_SetItem(pList, 0, pValue);

pValue = PyUnicode_DecodeUTF8("Hello", 5, NULL);
PyList_SetItem(pList, 1, pValue);

pValue = PyFloat_FromDouble(3.14);
PyList_SetItem(pList, 2, pValue);

/* Print list information */
print_python_list_info(pList);

/* Clean up and finalize Python */
Py_DECREF(pList);
Py_Finalize();
return (0);
}
