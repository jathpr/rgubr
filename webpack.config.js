const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');

module.exports = env => {
    const ifProd = plugin => env.prod
        ? plugin
        : undefined;
    const removeEmpty = array => array.filter(p => !!p);

    return {

        devtool: 'cheap-module-eval-source-map',

        entry: {
            app: path.join(__dirname, 'mapView'),
            vendor: ['react', 'react-dom', 'react-router']
        },
        // entry: './mapView/index.js',
        output: {
            path: path.join(__dirname, 'main/static'),
            filename: 'app.js'
        },

        module: { //Обновлено
            // preLoaders: [
            //     { //добавили ESlint в preloaders
            //         test: /\.js$/,
            //         loaders: ['eslint'],
            //         include: [path.resolve(__dirname, "mapView")]
            //     }
            // ],
            loaders: [
                { //добавили babel-loader

                    exclude: /node_modules/, // ingore /node_modules
                    loader: 'babel-loader',
                    query: {
                        cacheDirectory: true,
                        plugins: ['transform-runtime'],
                        presets: ['es2015', 'stage-0', 'react']
                    },
                    include: [path.resolve(__dirname, "mapView")],
                    test: /\.jsx?$/
                }
            ]
        },
        plugins: removeEmpty([
            new webpack.optimize.CommonsChunkPlugin({name: 'vendor', minChunks: Infinity, filename: '[name].[hash].js'}),


            // Only running DedupePlugin() and UglifyJsPlugin() in production
            ifProd(new webpack.optimize.DedupePlugin()),
            ifProd(new webpack.optimize.UglifyJsPlugin({
                compress: {
                    'screw_ie8': true,
                    'warnings': false,
                    'unused': true,
                    'dead_code': true
                },
                output: {
                    comments: false
                },
                sourceMap: false
            }))
        ])
    };
};
