mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"srd1908@cse.jgec.ac.in\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
