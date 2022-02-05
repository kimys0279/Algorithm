const setZeros = (r, c, matrix) => {
    for (let i = 0; i < matrix.length; i++){
        matrix[i][c] = 0;
    }
    
    for ( let i = 0; i < matrix[0].length; i++) {
        matrix[r][i] = 0;
    }
}

var setZeroes = function(matrix) {
    const zerosA = [];
    
    for (let r = 0; r < matrix.length; r++) {
        for (let c = 0; c < matrix[0].length; c++) {
            if (matrix[r][c] === 0) zerosA.push([r, c]);
            
        }
    }
    
    for (let address of zerosA) {
        let row = address[0];
        let col = address[1];
        setZeros(row, col, matrix);
    }
};