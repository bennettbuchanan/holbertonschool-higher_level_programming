//
//  ViewController.swift
//  SiliconValleyCompanies
//
//  Created by Bennett Buchanan on 5/26/16.
//  Copyright © 2016 Bennett Buchanan. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    let companies:[String] = ["Holberton", "Linkedin", "Docker", "Google", "Yahoo", "Apple"]
    
    func getTechCompanies() -> [String] {
        return companies
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}

