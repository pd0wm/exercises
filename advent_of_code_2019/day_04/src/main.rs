extern crate z3;
use z3::ast::Ast;
use z3::*;

fn main() {
    let cfg = Config::new();
    let ctx = Context::new(&cfg);
    let solver = Solver::new(&ctx);

    let num_vars : usize = 6;
    let mut vars = Vec::new();

    // Create variables
    for i in 0..num_vars {
        vars.push(ast::Int::new_const(&ctx, i.to_string()));
    }

    // Each number is between 0 and 9
    let zero = ast::Int::from_i64(&ctx, 0);
    let nine = ast::Int::from_i64(&ctx, 9);
    for var in &vars {
        solver.assert(&var.ge(&zero));
        solver.assert(&var.le(&nine));
    }

    // Compute decimal representation
    let mut decimal = zero;
    for i in 0..num_vars {
        let base : i64 = 10;
        let multiplier = ast::Int::from_i64(&ctx, base.pow(i as u32));
        decimal = decimal.add(&[&vars[i].mul(&[&multiplier])]);
    }

    // Assert start and end range
    let range_start = ast::Int::from_i64(&ctx, 347312);
    let range_end = ast::Int::from_i64(&ctx, 805915);
    solver.assert(&decimal.ge(&range_start));
    solver.assert(&decimal.le(&range_end));

    // Assert numbers increment
    for i in 1..num_vars {
        solver.assert(&vars[i-1].ge(&vars[i]));
    }

    // Part 1: Assert at least two adjacent numbers are equal
    let mut cond = vars[0]._eq(&vars[1]);
    for i in 1..num_vars-1 {
        cond = cond.or(&[&vars[i]._eq(&vars[i+1])]);
    }
    solver.assert(&cond);

    // Part 2: Assert only two adjecent numbers are equal
    let mut cond = ast::Bool::from_bool(&ctx, false);
    for i in 0..num_vars-1 {
        let mut a = vars[i]._eq(&vars[i+1]);

        if i > 0 {
            a = a.and(&[&vars[i]._eq(&vars[i-1]).not()]);
        }
        if i < num_vars - 2 {
            a = a.and(&[&vars[i+1]._eq(&vars[i+2]).not()]);
        }
        cond = cond.or(&[&a]);
    }
    solver.assert(&cond);

    // Get solutions
    let mut solutions = Vec::new();
    while solver.check() == SatResult::Sat {
        let model = solver.get_model();
        let decimal_solution = model.eval(&decimal).unwrap().as_i64().unwrap();

        // Exclude current solution from the set, and try to solve again
        solver.assert(&decimal._eq(&ast::Int::from_i64(&ctx, decimal_solution)).not());

        println!("{:?}", decimal_solution);
        solutions.push(decimal_solution);
    }

    println!("Number of passwords: {}", solutions.len());
}
