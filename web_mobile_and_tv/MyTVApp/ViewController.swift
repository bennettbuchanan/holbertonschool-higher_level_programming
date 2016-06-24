//
//  ViewController.swift
//  MyTVApp
//
//  Created by Bennett Buchanan on 6/24/16.
//  Copyright © 2016 Bennett Buchanan. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var shows_collection: UICollectionView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        var list: [MyTVAppItem] = []
        
        list[0].name = "Bip"
        list[0].url_stream = "http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8"
        
        list[1].name = "Apple Keynote"
        list[1].url_stream = "http://qthttp.apple.com.edgesuite.net/1010qwoeiuryfg/sl.m3u8"
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

