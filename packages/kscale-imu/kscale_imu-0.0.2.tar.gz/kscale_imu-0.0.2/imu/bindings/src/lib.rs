use hexmove::{ImuData as HexmoveImuData, ImuReader as HexmoveImuReader};
use pyo3::prelude::*;
use pyo3_stub_gen::define_stub_info_gatherer;
use pyo3_stub_gen::derive::{gen_stub_pyclass, gen_stub_pymethods};
use std::sync::{Arc, Mutex};

#[gen_stub_pyclass]
#[pyclass]
struct PyHexmoveImuReader {
    inner: Arc<Mutex<HexmoveImuReader>>,
}

#[gen_stub_pymethods]
#[pymethods]
impl PyHexmoveImuReader {
    #[new]
    fn new(interface: String, serial_number: u8, model: u8) -> PyResult<Self> {
        let imu_reader = HexmoveImuReader::new(&interface, serial_number, model)
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))?;
        Ok(PyHexmoveImuReader {
            inner: Arc::new(Mutex::new(imu_reader)),
        })
    }

    fn get_data(&self) -> PyResult<PyHexmoveImuData> {
        let imu_reader = self.inner.lock().unwrap();
        let data = imu_reader.get_data();
        Ok(PyHexmoveImuData::from(data))
    }

    fn stop(&self) -> PyResult<()> {
        let imu_reader = self.inner.lock().unwrap();
        imu_reader.stop();
        Ok(())
    }
}

#[gen_stub_pyclass]
#[pyclass]
#[derive(Clone)]
struct PyHexmoveImuData {
    #[pyo3(get)]
    x_angle: f32,
    #[pyo3(get)]
    y_angle: f32,
    #[pyo3(get)]
    z_angle: f32,
    #[pyo3(get)]
    x_velocity: f32,
    #[pyo3(get)]
    y_velocity: f32,
    #[pyo3(get)]
    z_velocity: f32,
}

impl From<HexmoveImuData> for PyHexmoveImuData {
    fn from(data: HexmoveImuData) -> Self {
        PyHexmoveImuData {
            x_angle: data.x_angle,
            y_angle: data.y_angle,
            z_angle: data.z_angle,
            x_velocity: data.x_velocity,
            y_velocity: data.y_velocity,
            z_velocity: data.z_velocity,
        }
    }
}

#[pymodule]
fn bindings(m: &Bound<PyModule>) -> PyResult<()> {
    m.add_class::<PyHexmoveImuReader>()?;
    m.add_class::<PyHexmoveImuData>()?;
    Ok(())
}

define_stub_info_gatherer!(stub_info);
