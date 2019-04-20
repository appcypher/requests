const path = require('path');
const webpack = require('webpack');
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');

module.exports = {
  mode: 'production',
  context: path.join(__dirname, '../client'),
  devtool: 'source-map',
  entry: [
    './index.js',
  ],
  output: {
    path: path.join(__dirname, '../client/dist'), // directory where bundle is dropped
    filename: 'bundle.min.js',
    publicPath: 'dist/', // directory where dev-server looks at for bundle
  },
  module: {
    rules: [{
      test: /\.jsx?$/,
      exclude: /node_modules/,
      resolve: { extensions: [".js", ".jsx"] },
      use: {
        loader: 'babel-loader',
        query: {
          presets: ['env', 'stage-1'],
        },
      },
    },
    {
      test: /\.css$/,
      use: ['style-loader', 'css-loader'],
    },
    {
      test: /\.html$/,
      use: ['html-loader'],
    },
    {
      test: /\.scss$/,
      use: ['style-loader', 'css-loader', 'sass-loader'],
    },
    {
      test: /\.(png|jpg|gif)$/,
      use: [
        {
          loader: 'file-loader',
          options: {},
        },
      ],
    },
    {
      test: /\.(ttf|eot|woff|woff2)(\?v=\d+\.\d+\.\d+)?$/,
      use: [
        {
          loader: 'url-loader',
          options: {},
        },
      ],
    },
    {
      test: /\.svg$/,
      loader: 'svg-inline-loader'
    }
    ],
  },
  plugins: [
    new UglifyJSPlugin({
      sourceMap: true,
    }),
  ],
};
