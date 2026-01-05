config = {
    "openai":{
        "api_key": "openai_key"
    },
    "Kafka":{
        "sasl.username":"conflunet cloud username",
        "sasl.password":"confluent cloud password",
        "bootstarp.server":"server url",
        "security.protocol":"SASL_SSL",
        "sasl.mechanisms":"PLAIN",
        "session.timeout.ms":5000
    },
    "schema_resigtry":{
        "url": "",
        "basic.auth.user.info":"username:password"
    }
}