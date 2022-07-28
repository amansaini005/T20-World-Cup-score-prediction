mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"amaner24@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
