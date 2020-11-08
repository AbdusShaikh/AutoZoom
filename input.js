function replacementLabels() {



    var textByLine = fsLibrary.readFileSync('meeting-name.txt').toString();
    console.log(textByLine);

        /* 
    fsLibrary.readFileSync('meeting-name.txt', (error, txtString) => {
    
        if (error) throw err;

        window.value = txtString.toString();
    })

    */
    

    fsLibrary.readFile('meeting-label.txt', (error, txtString) => {
        
        if (error) throw err;
        
        console.log(txtString.toString())
    
    })

    
    fsLibrary.readFile('meeting-time.txt', (error, txtString) => {
        
        if (error) throw err;
        
        console.log(txtString.toString())
    
    })

    


};