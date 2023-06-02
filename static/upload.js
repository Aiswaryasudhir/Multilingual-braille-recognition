# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:51:28 2023

@author: AISWARYA
"""

function readURL(input) {
if (input.files && input.files[0]) {
    var reader = new FileReader();
  
    reader.onload = function (e) {
        $('#blah')
            .attr('src', e.target.result)
            .width(150)
            .height(200);
    };
  
    reader.readAsDataURL(input.files[0]);
}
}