//
//  TechCompaniesListViewController.swift
//  TechCompanies
//
//  Created by Bennett Buchanan on 6/8/16.
//  Copyright © 2016 Bennett Buchanan. All rights reserved.
//

import UIKit

class TechCompaniesListViewController: UITableViewController {
    
    var schoolList:[Entity]!
    var techCompanyList:[Entity]!
    var completeList:[Entity]!
    var uniqueType:[String] = []
    var i: Int = 0
    var town: Bool = false
    
    let techDetailSegue = "techDetailSegue"
    
    func toggle () {
        if town == true {
            town = false
        } else {
            town = true
        }
        
        uniqueType.removeAll()
        self.tableView.reloadData()
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.title = "Entity list"
        techCompanyList = EntitiesHelper.getTechCompanies()
        schoolList = EntitiesHelper.getSchools()
        completeList = EntitiesHelper.getEntireList()
        

        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // self.navigationItem.rightBarButtonItem = self.editButtonItem()
        
        self.navigationItem.rightBarButtonItem = UIBarButtonItem(title: "Toggle", style: .Plain, target: self, action: #selector(toggle))
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        
        // Determine how many sections should be in the list.
        for e in completeList {
            if town == true {
                if uniqueType.contains(e.town) {
                } else {
                    uniqueType.append(e.town)
                }
            } else if town == false {
                if uniqueType.contains(e.type.rawValue) {
                } else {
                    uniqueType.append(e.type.rawValue)
                }
            }
        }
        
        // Return the unique types to break the list into section.
        return uniqueType.count
    }

    override func tableView(tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        
        // Detmine the title for the appropriate section.
        var i = 0
        for index in 0...(uniqueType.count - 1) {
            if index == section {
                break
            } else {
                i += 1
            }
        }
        
        // Return the title based on the uniqueType array.
        return uniqueType[i]
    }
    
    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        
        // Determine the number of rows for the appropriate section based on the value of uniqueType.
        var i = 0
        for index in 0...(uniqueType.count - 1) {
            if index == section {
                for e in completeList {
                    if town == true {
                        if e.town == uniqueType[index] {
                            i += 1
                        }
                    } else if town == false {
                        if e.type.rawValue == uniqueType[index] {
                            i += 1
                        }
                    }
                }
                break
            }
        }
        
        // Return the number of rows.
        return i
    }

    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("techCell", forIndexPath: indexPath)

        // Set i to 0.
        i = 0

        // Find the index in the uniqueType
        for index in 0...(uniqueType.count - 1) {
            if index == indexPath.section {
                for e in completeList {
                    // Find the corresponding type string.
                    if town == true {
                        if e.town == uniqueType[indexPath.section] {
                            if indexPath.row == i {
                                cell.textLabel?.text = e.name
                                cell.imageView?.image = UIImage(named: e.imageName)
                                if e.name == "Holberton" {
                                    cell.detailTextLabel?.text = "I love studying"
                                } else {
                                    cell.detailTextLabel?.text = "I love working"
                                }
                                break
                            } else {
                                i += 1
                            }
                        }
                    } else if town == false {
                        if e.type.rawValue == uniqueType[indexPath.section] {
                            if indexPath.row == i {
                                cell.textLabel?.text = e.name
                                cell.imageView?.image = UIImage(named: e.imageName)
                                if uniqueType[indexPath.section] == "School" {
                                    cell.detailTextLabel?.text = "I love studying"
                                } else {
                                    cell.detailTextLabel?.text = "I love working"
                                }
                                break
                            } else {
                                i += 1
                            }
                        }
                    }
                }
            }
        }

        return cell
    }


    // Override to support conditional editing of the table view.
    override func tableView(tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }

    /*
    // Override to support editing the table view.
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        if editingStyle == .Delete {
            // Delete the row from the data source
            tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Fade)
        } else if editingStyle == .Insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    // Override to support rearranging the table view.
    override func tableView(tableView: UITableView, moveRowAtIndexPath fromIndexPath: NSIndexPath, toIndexPath: NSIndexPath) {

    }

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the item to be re-orderable.
        return true
    }
    */


    // MARK: - Navigation
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == "techDetailSegue" {
            if let destination = segue.destinationViewController as? TechCompanyDetailViewController {
                
                let path = tableView.indexPathForSelectedRow
                
                // Set i to 0.
                i = 0
                
                // Find the index in the uniqueType
                for index in 0...(uniqueType.count - 1) {
                    if index == path!.section {
                        for e in completeList {
                            // Find the corresponding type string.
                            if town == true {
                                if e.town == uniqueType[path!.section] {
                                    if path!.row == i {
                                        destination.entity = e
                                        break
                                    } else {
                                        i += 1
                                    }
                                }
                            } else if town == false {
                                if e.type.rawValue == uniqueType[path!.section] {
                                    if path!.row == i {
                                        destination.entity = e
                                        break
                                    } else {
                                        i += 1
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
//    // In a storyboard-based application, you will often want to do a little preparation before navigation
//    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
//        // Get the new view controller using segue.destinationViewController.
//        // Pass the selected object to the new view controller.
//        if segue.identifier == "techDetailSegue" {
//            let _ = segue.destinationViewController as? TechCompanyDetailViewController
//        }
//    }
}
