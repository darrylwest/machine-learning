#!/usr/bin/env node

// dpw@alameda.local
// 2015.03.04
'use strict';

const fs = require( 'fs' ),
    dash = require( 'lodash' ),
    spawn = require( 'child_process' ).spawn;

let files = new Set(),
    tid,
    lastRun = Date.now();

const spawnJob = function( runner ) {
    runner.stdout.on( 'data', function( data ) {
        process.stdout.write( data );
    } );

    runner.stderr.on( 'data', function( data ) {
        process.stdout.write( data );
    } );

    runner.on( 'close', function( code ) {
        if ( code !== 0 ) {
            console.log( 'did not exit correctly, code: ', code );
        }

        tid = null;
    } );
};

const run = function() {
    console.log( '[H[2J' );
    console.log( 'files: ', files );
    console.log( '------------------------------------ last run: ', new Date().toISOString() );

    spawnJob( spawn( 'make', [ 'test' ] ));

    files.clear();
};

const changeHandler = function( event, filename ) {

    // this could create dups, but better that than to miss a file...
    if ( dash.endsWith( filename, '.py' ) ) {
        files.add( filename );
    }

    if ( files.size > 0 && !tid ) {
        tid = setTimeout( function() {
            run();
        }, 250 );
    }
};

fs.watch( './lib/', {recursive: false}, changeHandler );
fs.watch( './tests/', {recursive: false}, changeHandler );

console.log( 'watcher started...' );
run();
