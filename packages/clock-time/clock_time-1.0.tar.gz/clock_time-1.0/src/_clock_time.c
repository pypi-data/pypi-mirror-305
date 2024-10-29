#include "Python.h"

#include <time.h>

#if !defined(CLOCK_MONOTONIC) || \
    !defined(CLOCK_REALTIME) || \
    !defined(TIMER_ABSTIME)
    #error "clock_nanosleep() function is not available on this platform."
#endif

#define SEC_TO_NS (1000*1000*1000)

inline static int
_a_LE_b(const struct timespec *a, const struct timespec *b)
{
    if (a->tv_sec < b->tv_sec ||
        (a->tv_sec  == b->tv_sec &&
         a->tv_nsec <= b->tv_nsec)) {
        return 1;
    }
    return 0;
}

inline static int
_get_time(clockid_t clk_id, struct timespec *ts)
{
    if (clock_gettime(clk_id, ts) == 0) {
        return 0;
    } else {
        PyErr_SetFromErrno(PyExc_OSError);
        return -1;
    }
}

static PyObject *
_sleep(PyObject *module, PyObject *obj)
{
    struct timespec monotonic, deadline;

    /* get monotonic */
    if (_get_time(CLOCK_MONOTONIC, &monotonic)) {
        return NULL;
    }

    /* get seconds from arg, and calculate deadline. */
    if (PyFloat_Check(obj)) {
        int64_t nsec, add_sec;
        double d = PyFloat_AsDouble(obj);

        if (isnan(d) || d < 0.0 || d >= (double)(INT64_MAX / SEC_TO_NS)) {
            goto secs_out_of_range;
        }
        nsec = (int64_t)(d * SEC_TO_NS);
        if (nsec == 0) {
            Py_RETURN_NONE;
        }

        /* calculate deadline */
        add_sec = nsec / SEC_TO_NS;
        if (sizeof(deadline.tv_sec) == 4 && add_sec > (int64_t)INT32_MAX) {
            goto secs_out_of_range;
        }
        deadline.tv_sec  = monotonic.tv_sec  + add_sec;
        deadline.tv_nsec = monotonic.tv_nsec + (nsec % SEC_TO_NS);
        if (deadline.tv_nsec >= SEC_TO_NS) {
            deadline.tv_sec  += 1;
            deadline.tv_nsec -= SEC_TO_NS;
        }
    } else {
        int64_t sec = PyLong_AsLongLong(obj);
        if (sec < 0) {
            if (sec == -1 && PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError,
                                "Can't covert secs to int64_t");
                return NULL;
            }
            goto secs_out_of_range;
        }
        if (sec == 0) {
            Py_RETURN_NONE;
        }

        /* calculate deadline */
        if (sizeof(deadline.tv_sec) == 4 && sec > (int64_t)INT32_MAX) {
            goto secs_out_of_range;
        }
        deadline.tv_sec  = monotonic.tv_sec + sec;
        deadline.tv_nsec = monotonic.tv_nsec;
    }

    /* check overflow */
    if (_a_LE_b(&deadline, &monotonic)) {
        /* deadline <= monotonic. in fact can't be equal. */
        goto secs_out_of_range;
    }

    /* sleep */
    while (1) {
        int ret;

        Py_BEGIN_ALLOW_THREADS
        ret = clock_nanosleep(CLOCK_MONOTONIC, TIMER_ABSTIME,
                              &deadline, NULL);
        Py_END_ALLOW_THREADS

        /* success */
        if (ret == 0) {
            Py_RETURN_NONE;
        }

        if (ret != EINTR) {
            errno = ret;
            PyErr_SetFromErrno(PyExc_OSError);
            return NULL;
        }

        /* sleep was interrupted by SIGINT */
        if (PyErr_CheckSignals()) {
            return NULL;
        }

        /* check timeout */
        if (_get_time(CLOCK_MONOTONIC, &monotonic)) {
            return NULL;
        }
        if (_a_LE_b(&deadline, &monotonic)) {
            /* deadline <= monotonic */
            Py_RETURN_NONE;
        }
    }

secs_out_of_range:
    PyErr_SetString(PyExc_ValueError,
                    "Secs is negative/overflow/out_of_range.");
    return NULL;
}

static PyObject *
_time_s(PyObject *module, PyObject *Py_UNUSED(unused))
{
    struct timespec ts;

    /* get time */
    if (_get_time(CLOCK_REALTIME, &ts)) {
        return NULL;
    }
    return PyLong_FromLongLong((int64_t)ts.tv_sec);
}

static PyMethodDef _clock_time_methods[] = {
    {"sleep",  (PyCFunction)_sleep,  METH_O, NULL},
    {"time_s", (PyCFunction)_time_s, METH_NOARGS, NULL},
    {0}
};

static PyModuleDef _clock_time_module = {
    PyModuleDef_HEAD_INIT,
    .m_name = "_clock_time",
    .m_size = 0,
    .m_methods = _clock_time_methods,
};

PyMODINIT_FUNC
PyInit__clock_time(void)
{
    return PyModule_Create(&_clock_time_module);
}
