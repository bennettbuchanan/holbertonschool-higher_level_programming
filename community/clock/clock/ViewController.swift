//
//  ViewController.swift
//  clock
//
//  Created by Bennett Buchanan on 6/14/16.
//  Copyright © 2016 Bennett Buchanan. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var clock_label: UILabel!
    @IBOutlet weak var pie_message: UILabel!
    
    var timer = NSTimer()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Add the message for the clock.
        pie_message.text = "Time for pie."
        
        generate_clock("minute");
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func generate_clock(clock_style: String) {
        if clock_style == "second" {
            self.timer = NSTimer.scheduledTimerWithTimeInterval(0.1,
                                                                target: self,
                                                                selector: #selector(second),
                                                                userInfo: nil,
                                                                repeats: true)
        } else {
            self.timer = NSTimer.scheduledTimerWithTimeInterval(0.1,
                                                                target: self,
                                                                selector: #selector(minute),
                                                                userInfo: nil,
                                                                repeats: true)
        }
    }
    
    func second() {
        clock_label.text = NSDateFormatter.localizedStringFromDate(NSDate(), dateStyle: .NoStyle, timeStyle: .MediumStyle)
    }
    
    func minute() {
        clock_label.text = NSDateFormatter.localizedStringFromDate(NSDate(), dateStyle: .NoStyle, timeStyle: .ShortStyle)
    }

}

