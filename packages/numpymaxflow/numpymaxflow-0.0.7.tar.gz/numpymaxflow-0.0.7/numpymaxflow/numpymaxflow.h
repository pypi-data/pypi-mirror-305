// Copyright (c) 2022, Muhammad Asad (masadcv@gmail.com)
// All rights reserved.

// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:

// 1. Redistributions of source code must retain the above copyright notice, this
//    list of conditions and the following disclaimer.

// 2. Redistributions in binary form must reproduce the above copyright notice,
//    this list of conditions and the following disclaimer in the documentation
//    and/or other materials provided with the distribution.

// 3. Neither the name of the copyright holder nor the names of its
//    contributors may be used to endorse or promote products derived from
//    this software without specific prior written permission.

// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
// FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
// DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
// SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
// CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
// OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#pragma once

#include "common.h"


void maxflow2d_cpu(
    const float *image_ptr,
    const float *prob_ptr,
    float *label_ptr, // returned argument
    const int &channel,
    const int &height,
    const int &width,
    const float &lambda,
    const float &sigma,
    const int &connectivity);

void maxflow3d_cpu(
    const float *image_ptr,
    const float *prob_ptr,
    float *label_ptr, // returned argument
    const int &channel,
    const int &depth,
    const int &height,
    const int &width,
    const float &lambda,
    const float &sigma,
    const int &connectivity);

static PyObject *
maxflow_wrapper(PyObject *self, PyObject *args);

void add_interactive_seeds_2d(
    float *prob_ptr, 
    const float *seed_ptr,
    const int &channel, 
    const int &height, 
    const int &width);

void add_interactive_seeds_3d(
    float *prob_ptr, 
    const float *seed_ptr,
    const int &channel, 
    const int &depth, 
    const int &height, 
    const int &width);


static PyObject *
maxflow_interactive_wrapper(PyObject *self, PyObject *args);
        

static PyMethodDef methods[] = {
    {"maxflow",  maxflow_wrapper, METH_VARARGS, "computing 2D/3D maxflow"},
    {"maxflow_interactive",  maxflow_interactive_wrapper, METH_VARARGS, "computing 2D/3D interactive maxflow with interactions"},
    {NULL, NULL, 0, NULL}
};

static PyModuleDef maxflow_module = { 
	PyModuleDef_HEAD_INIT, "numpymaxflowcpp", NULL, -1, methods
};


PyMODINIT_FUNC PyInit_numpymaxflowcpp(void)
{
	import_array();
	return PyModule_Create (&maxflow_module);
}