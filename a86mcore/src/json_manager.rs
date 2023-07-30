use serde::{Deserialize, Serialize};
use serde_json::{Map, Number, Result};
use std::fs;

#[derive(Serialize, Deserialize)]
struct MonitorConfig {
    emails: Vec<String>,
    password: String,
    sender: String,
    sender_name: String,
    sender_port: u8,
    sender_server: String,
    name: String,
    email_mode: String,
    use_influx: bool,
    db_username: String,
    db_password: String,
    db_port: u8,
    db_name: String

}

struct Target{
    target_type: String,
    target: String,
    enabled: bool
}

enum Value {
    Null,
    Bool(bool),
    Number(Number),
    String(String),
    Array(Vec<Value>),
    Object(Map<String, Value>),
}

fn read_target_file() -> Value
{
    let target_json = fs::read_to_string("targets.json").expect("Unable to read file")
        .as_str();
    let v: Value = serde_json::from_str(target_json)?;
    return v;
}

fn read_monitor_file() -> MonitorConfig
{
    let monitor_json = fs::read_to_string("monitor.json").expect("Could not read file")
        .as_str();
    let obt_monitor_config: MonitorConfig = serde_json::from_str(monitor_json)?;
    return obt_monitor_config;
}

fn resolve_targets(target_json: Value) -> Vec<Target>
{
    let mut res_target:Vec<Target> = Vec::new();
    for obt_target in target_json["target-list"]
    {
        let new_target = Target{
            target_type: target_json[obt_target]["type"],
            target: target_json[obt_target]["target"],
            enabled: target_json[obt_target]["enabled"]
        };
        res_target.push(new_target);
    }
    return res_target;
}

