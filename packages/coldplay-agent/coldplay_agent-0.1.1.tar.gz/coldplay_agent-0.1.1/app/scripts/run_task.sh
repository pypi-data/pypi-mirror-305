#!/bin/bash

reboot_needed=0
pointfoot_repo=$1
script_run_url_new=$2
project_file_uri=$3
task_id=$4
code_type=$5
version_type=$6
version_name=$7

# bash fonts colors
red='\e[31m'
yellow='\e[33m'
gray='\e[90m'
green='\e[92m'
blue='\e[94m'
magenta='\e[95m'
cyan='\e[96m'
none='\e[0m'
_red() { echo -e ${red}$@${none}; }
_blue() { echo -e ${blue}$@${none}; }
_cyan() { echo -e ${cyan}$@${none}; }
_green() { echo -e ${green}$@${none}; }
_yellow() { echo -e ${yellow}$@${none}; }
_magenta() { echo -e ${magenta}$@${none}; }
_red_bg() { echo -e "\e[41m$@${none}"; }

is_err=$(_red_bg 错误：)
is_warn=$(_red_bg 警告：)
is_info=$(_red_bg 提示：)

err() {
    echo -e "\n$is_err $@\n" && exit 1
}

warn() {
    echo -e "\n$is_warn $@\n"
}

info() {
    echo -e "\n$is_info $@\n"
}

check_err() {
    if [[ $? != 0 ]]; then echo -e "\n$is_err $@\n" && exit 1; fi
}

if [[ $(lsb_release -rs) != "20.04" || $(lsb_release -is) != "Ubuntu" || $(uname -m) != "x86_64" ]]; then
    err "仅支持 ${yellow}(Ubuntu 20.04 和 x86_64 架构)${none}"
fi

conda_activate_pointfoot_legged_gym() {
    local anaconda_dir="$HOME/anaconda3"

    __conda_setup="$('$anaconda_dir/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
        # Use eval to apply Conda setup if successful
        eval "$__conda_setup"
    else
        if [ -f "$anaconda_dir/etc/profile.d/conda.sh" ]; then
            # Source the conda.sh script if it exists
            . "$anaconda_dir/etc/profile.d/conda.sh"
        else
            # Fallback to adding Conda to PATH if other methods fail
            export PATH="$anaconda_dir/bin:$PATH"
        fi
    fi
    unset __conda_setup

    # Activate the newly created environment
    info "${yellow}激活 Conda 环境 pointfoot_legged_gym..."
    conda activate pointfoot_legged_gym
    check_err "${yellow}激活 Conda 环境 pointfoot_legged_gym失败"
}

install_pointfoot_legged_gym() {
    info "${yellow}开始安装pointfoot-legged-gym..."

    sleep 3

    conda_activate_pointfoot_legged_gym

    local conda_env="pointfoot_legged_gym"
    local rl_dir="$HOME/limx_rl/$task_id"
    local back_dir="$HOME/limx_rl/bak"

    mkdir -p "$rl_dir"
    mkdir -p "$back_dir"

    # Install pointfoot-legged-gym
    info "${yellow}安装 pointfoot-legged-gym 库 ..."
    cd $rl_dir
    info "wget:$pointfoot_repo"
    filename=$(basename "$project_file_uri")
    name_without_extension_filename="${filename%.*}"
    wget -O $filename "$pointfoot_repo"
    info "filename:$filename"
    #mac环境压缩会多出这一部分，删除掉
    if [ -d "$rl_dir/__MACOSX" ]; then
        rm -rf "$rl_dir/__MACOSX"
        info "已删除目录 $rl_dir/__MACOSX"
    else
        info "目录 $rl_dir/__MACOSX 不存在"
    fi
    # if [ ! -d "$rl_dir/pointfoot-legged-gym" ]; then
    #     unzip "$rl_dir/$filename"
    # else
    #     tar -czf "$back_dir/pointfoot-legged-gym-$(date +%Y%m%d%H%M%S).tar.gz" $rl_dir/pointfoot-legged-gym
    #     rm -rf "$rl_dir/pointfoot-legged-gym"
    #     unzip "$rl_dir/$filename"
    # fi
    unzip -o "$rl_dir/$filename"
    rm -rf "$rl_dir/$filename"
    
    last_folder=$(ls -d */ | tail -n 1)
    last_folder_name=${last_folder%/}

    cd "$rl_dir/$last_folder_name"
    pip install -e .
    check_err "${yellow}安装 pointfoot-legged-gym 库失败"
    info "${yellow}安装 pointfoot-legged-gym 库成功"
}


install_pointfoot_legged_gym_from_git() {
    info "${yellow}开始安装pointfoot-legged-gym..."

    sleep 3

    conda_activate_pointfoot_legged_gym

    local conda_env="pointfoot_legged_gym"
    local rl_dir="$HOME/limx_rl/$task_id"
    local back_dir="$HOME/limx_rl/bak"

    mkdir -p "$rl_dir"
    mkdir -p "$back_dir"

    # Install pointfoot-legged-gym
    info "${yellow}安装 pointfoot-legged-gym 库 ..."
    cd $rl_dir
    if [ ! -d "$rl_dir/pointfoot-legged-gym" ]; then
        if [ "$version_type" == "1" ]; then
            #分支
            git clone -b $version_name "$pointfoot_repo"
        elif [ "$version_type" == "2" ]; then
            #提交
            git clone "$pointfoot_repo"
            last_folder1=$(ls -d */ | tail -n 1)
            last_folder_name1=${last_folder1%/}
            cd "$rl_dir/$last_folder_name1"
            git checkout $version_name
        else
            #tag
            git clone "$pointfoot_repo"
            last_folder1=$(ls -d */ | tail -n 1)
            last_folder_name1=${last_folder1%/}
            cd "$rl_dir/$last_folder_name1"
            git checkout $version_name
        fi
    fi
    last_folder=$(ls -d */ | tail -n 1)
    last_folder_name=${last_folder%/}
    cd "$rl_dir/$last_folder_name"
    pip install -e .
    check_err "${yellow}安装 pointfoot-legged-gym 库失败"
    info "${yellow}安装 pointfoot-legged-gym 库成功"
}

run_task() {
    info "${yellow} - 激活pointfoot_legged_gym的conda环境"

    sleep 3

    conda_activate_pointfoot_legged_gym

    local conda_env="pointfoot_legged_gym"
    local rl_dir="$HOME/limx_rl/$task_id"
    cd $rl_dir
    last_folder=$(ls -d */ | tail -n 1)
    last_folder_name=${last_folder%/}

    # 无头模式下继续训练
    cd "$rl_dir/$last_folder_name"
    info "$rl_dir/$last_folder_name"
    #python legged_gym/scripts/train.py --task=pointfoot_rough --headless
    nohup python $script_run_url_new --task=pointfoot_rough --task_id=$task_id --headless > ./pointfoot_legged_gym_output.log 2>&1 &
    check_err "${yellow}运行失败"
    info "${yellow}运行成功"
}

# 根据code_type判断执行哪个安装函数 如果为1则代码安装 如果为2则git安装
info "code_type：${code_type}"
if [ "$code_type" == "1" ]; then
    info "${yellow}压缩包安装 pointfoot-legged-gym 库"
    install_pointfoot_legged_gym
elif [ "$code_type" == "2" ]; then
    info "${yellow}git安装 pointfoot-legged-gym 库"
    install_pointfoot_legged_gym_from_git
else
    err "无效的code_type: $code_type"
fi

run_task


