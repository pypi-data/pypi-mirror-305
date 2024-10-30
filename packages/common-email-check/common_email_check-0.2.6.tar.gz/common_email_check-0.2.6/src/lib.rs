use pyo3::prelude::*;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use tokio::sync::Semaphore;
use std::sync::Arc;
use futures::future;
use check_if_email_exists::{check_email, CheckEmailInput};

// 이메일 검증을 위한 구조체
#[derive(Debug, Deserialize, Serialize)]
struct Record {
    email: String,
}

#[derive(Debug, Serialize)]
struct ResultRecord {
    email: String,
    result: String,
}

#[pyfunction]
fn process_emails(py_records: Vec<Option<String>>) -> PyResult<Vec<(String, String)>> {
    let rt = tokio::runtime::Runtime::new().unwrap();
    let result = rt.block_on(async move {
        let semaphore = Arc::new(Semaphore::new(150));
        let tasks: Vec<_> = py_records
            .into_iter()
            .map(|email_opt| {
                let semaphore = semaphore.clone();
                tokio::spawn(async move {
                    let permit = semaphore.acquire_owned().await.unwrap();

                    // None 값을 빈 문자열로 처리
                    let email = email_opt.unwrap_or_default();
                    let input = CheckEmailInput::new(email.clone());
                    let result = check_email(&input).await;
                    drop(permit);

                    (email, format!("{:?}", result))
                })
            })
            .collect();

        let results: Vec<(String, String)> = future::join_all(tasks)
            .await
            .into_iter()
            .filter_map(|res| res.ok())
            .collect();
        results
    });

    Ok(result)
}

/// Python 모듈 정의
#[pymodule]
fn common_email_check(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(process_emails, m)?)?;
    Ok(())
}
