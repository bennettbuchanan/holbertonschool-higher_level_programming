//
//  ViewController.swift
//  TapperProject
//
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var image_tapper: UIImageView!
    @IBOutlet weak var button_play: UIButton!
    @IBOutlet weak var textfield_number: UITextField!
    @IBOutlet weak var label_taps: UILabel!
    @IBOutlet weak var button_coin: UIButton!

    var taps_requested: Int = 0
    
    @IBAction func clickPlayButton(sender: AnyObject) {
        let text: String = textfield_number.text!
        let int: Int? = Int(text)
        
        if int != nil && int > 0 {
            taps_requested = int!
            self.initGame()
            print("Let's do \(int!) taps")
        }
    }

    var taps_done: Int = 0
    
    @IBAction func clickCoinButton(sender: AnyObject) {
        print("Tap!")
        taps_done += 1
        label_taps.text = String(taps_done)
        if taps_done >= taps_requested {
            self.resetGame()
        }
    }
    
    func initGame() {
        button_play.hidden = true
        image_tapper.hidden = true
        textfield_number.hidden = true
        label_taps.hidden = false
        button_coin.hidden = false
        label_taps.text = "0"
    }
    
    func resetGame() {
        taps_requested = 0
        taps_done = 0
        label_taps.hidden = true
        button_coin.hidden = true
        image_tapper.hidden = false
        button_play.hidden = false
        textfield_number.hidden = false
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

