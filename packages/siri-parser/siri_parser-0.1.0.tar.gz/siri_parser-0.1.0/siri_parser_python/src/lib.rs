use pyo3::prelude::*;
use parser::{SIRI as SIRIParser, Envelope};

#[pyclass]
pub struct SIRI {}

#[pymethods]
impl SIRI {
    #[new]
    pub fn new() -> Self {
        SIRI {}
    }

    pub fn parse(&self, s: &str) -> PyResult<PyObject> {
        Python::with_gil(|py| {
            match SIRIParser::from_str::<Envelope>(s) {
                Ok(envelope) => Ok(envelope.into_py(py)),
                Err(e) => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(e.to_string()))
            }
        })
    }
}

#[pymodule]
fn siri_parser_python(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<SIRI>()?;
    Ok(())
}