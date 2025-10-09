
#!/bin/bash

# Check if exactly two arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <domain1> <domain2>"
    exit 1
fi

domain1=$1
domain2=$2

echo "Checking domains:"
echo "1. $domain1"
echo "2. $domain2"
echo ""

# Function to check if a domain is reachable
check_domain() {
    local domain=$1
    echo "Pinging $domain..."
    if ping -c 1 -W 2 "$domain" > /dev/null 2>&1; then
        echo " $domain is reachable"
    else
        echo " $domain is not reachable"
    fi
    echo ""
}

# Check both domains
check_domain "$domain1"
check_domain "$domain2"

fi
