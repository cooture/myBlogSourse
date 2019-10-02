---
title: zsh_is_too_slow
tags: ['zsh', 'linux']
date: 2019-09-30 19:54:28
categories: ['zsh']
---

# zsh慢成💩

> 简单介绍一下，Catalina升级成zsh之后，便安装了传说中最简单配置zsh的“插件”——oh-my-zsh
>
> 但是安装好之后，速度慢的像坨翔
>
> 启动五秒
>
> 随便cd一下要三秒
>
> 随便ls一下等两秒
>
> 啊
>
> 要死了

## Why

百度谷歌一番发现普遍都有这个问题，可能原因有很多，简单的原因这里不多说，建议先谷歌一下

问题集中在zsh的插件众多，每次执行时都会执行各种插件的东西，尤其是以git为最大的罪魁祸首。

所以，解决问题的第一步是先跟踪，定位问题。

```bash
zsh -xv
```

一般情况下可以发现慢的主要原因是卡在了git有关的命令上，关闭git插件后，没有任何影响，你会发现，git相关的命令是集成在主题上的，你可能可以通过使用下面的命令解决一定的问题，但是对于我来说可能不太有用

```bash
git config --global oh-my-zsh.hide-status 1
```

索性查看相关主题的配置源码，我用的主题是`fishy`

```bash
  1 # ZSH Theme emulating the Fish shell's default prompt.
  2 
  3 _fishy_collapsed_wd() {
  4   echo $(pwd | perl -pe '
  5    BEGIN {
  6       binmode STDIN,  ":encoding(UTF-8)";
  7       binmode STDOUT, ":encoding(UTF-8)";
  8    }; s|^$ENV{HOME}|~|g; s|/([^/.])[^/]*(?=/)|/$1|g; s|/\.([^/])[^/]*(?=/)|/.$1|g
  9 ')
 10 }
 11 
 12 local user_color='green'; [ $UID -eq 0 ] && user_color='red'
 13 PROMPT='%n@%m %{$fg[$user_color]%}$(_fishy_collapsed_wd)%{$reset_color%}%(!.#.>) '
 14 PROMPT2='%{$fg[red]%}\ %{$reset_color%}'
 15 
 16 local return_status="%{$fg_bold[red]%}%(?..%?)%{$reset_color%}"
 17 #RPROMPT="${RPROMPT}"'${return_status}$(git_prompt_info)$(git_prompt_status)%{$reset_color%}'
 18 
 19 ZSH_THEME_GIT_PROMPT_PREFIX=" "
 20 ZSH_THEME_GIT_PROMPT_SUFFIX=""
 21 ZSH_THEME_GIT_PROMPT_DIRTY=""
 22 ZSH_THEME_GIT_PROMPT_CLEAN=""
 23 
 24 ZSH_THEME_GIT_PROMPT_ADDED="%{$fg_bold[green]%}+"
 25 ZSH_THEME_GIT_PROMPT_MODIFIED="%{$fg_bold[blue]%}!"
 26 ZSH_THEME_GIT_PROMPT_DELETED="%{$fg_bold[red]%}-"
 27 ZSH_THEME_GIT_PROMPT_RENAMED="%{$fg_bold[magenta]%}>"
 28 ZSH_THEME_GIT_PROMPT_UNMERGED="%{$fg_bold[yellow]%}#"
 29 ZSH_THEME_GIT_PROMPT_UNTRACKED="%{$fg_bold[cyan]%}?"
```

发现git相关的命令集成在`RPROMPT="${RPROMPT}"'${return_status}$(git_prompt_info)$(git_prompt_status)%{$reset_color%}'`索性全部注释掉

## 爽

