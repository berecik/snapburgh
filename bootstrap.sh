#!/usr/bin/env bash

# create package.json file
cp -v package_src.json package.json

# React runtime library
npm i -S react react-dom

# Flickity component for pictures carousel
# currently unused
# npm i -S flickity react-flickity-component

# Webpack
npm i -D webpack webpack-cli webpack-bundle-tracker

# Babel
# state for 13.03.2020.
# babel-loader must be in 7 version due babel-core dependencies
# TODO: fix this if will change babel-core dependencies
npm i -D babel-loader@7
# rest of babel dependencies
npm i -D babel-core babel-preset-env babel-preset-react

# SASS and style loader
npm i -D node-sass sass-loader style-loader css-loader mini-css-extract-plugin sass

# React translation support https://github.com/i18next/react-i18next
npm i -S react-i18next
npm i -D babel-plugin-i18next-extract