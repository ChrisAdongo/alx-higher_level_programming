#ifndef PYTHON_H
#define PYTHON_H

typedef struct _object PyObject;
typedef struct _varobject PyVarObject;
typedef struct _bytesobject PyBytesObject;
typedef struct _typeobject PyTypeObject;
typedef struct _listobject PyListObject;

#define PyBytes_Check(obj) 1
#define PyList_Check(obj) 1
#define PyVarObject_HEAD_INIT(type, size) { PyObject_HEAD_INIT(type) size }

struct _object {
    PyTypeObject *ob_type;
};

struct _varobject {
    PyObject ob_base;
    Py_ssize_t ob_size;
};

struct _bytesobject {
    PyVarObject ob_base;
    char *ob_sval;
};

struct _typeobject {
    const char *tp_name;
};

struct _listobject {
    PyVarObject ob_base;
    PyObject *ob_item[10];
    long allocated;
};

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

#endif /* PYTHON_H */
