chr() {
    printf \\$(printf '%03o' $1)
}

function hex() {
    printf '%02X\n' $1
}

function dec() {
    printf '%02d\n' 0x$1
}

function encrypt() {
    key=$1
    msg=$2
    crpt_msg=""
    for ((i=0; i<${#msg}; i++)); do
        c=${msg:$i:1}
        asc_chr=$(echo -ne "$c" | od -An -tuC)
        key_pos=$((${#key} - 1 - ${i}))
        key_char=${key:$key_pos:1}
        crpt_chr=$(( $asc_chr ^ ${key_char} ))
        hx_crpt_chr=$(hex $crpt_chr)
        crpt_msg=${crpt_msg}${hx_crpt_chr}
    done
    echo $crpt_msg
}

function get_key() {
    msg=$1
    crpt_msg=$2
    rev_key=""
    for ((i=0; i<${#msg}; i++)); do
        c=${msg:$i:1}
        asc_chr=$(echo -ne "$c" | od -An -tuC)
        pos=$((${i} * 2))
        hx_crpt_chr=${crpt_msg:$pos:2}
        crpt_chr=$(dec $hx_crpt_chr)
        key_char=$(( $asc_chr ^ $crpt_chr ))
        rev_key=${rev_key}${key_char}
    done
    key=$(echo $rev_key | rev)
    echo $key
}

function decrypt() {
    rev_key=$1
    crpt_msg=$2
    key=$(echo $rev_key | rev)
    msg=""
    for ((i=0; i<${#key}; i++)); do
        key_char=${key:$i:1}
        pos=$((${i} * 2))
        hx_crpt_chr=${crpt_msg:$pos:2}
        crpt_chr=$(dec $hx_crpt_chr)
        asc_char=$(( $crpt_chr ^ ${key_char} ))
        c=$(chr $asc_char)
        msg=${msg}${c}
    done
    echo $msg
}

key=$(get_key "514;248;980;347;145;332" "3633363A33353B393038383C363236333635313A353336")
plain=$(decrypt $key "3A3A333A333137393D39313C3C3634333431353A37363D")
echo $plain
