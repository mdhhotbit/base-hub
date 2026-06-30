
pragma solidity 0.5.16;

interface IBEP20 {
  function totalSupply() external view returns (uint256);
  function decimals() external view returns (uint8);
  function symbol() external view returns (string memory);
  function name() external view returns (string memory);
  function getOwner() external view returns (address);
  function balanceOf(address account) external view returns (uint256);
  function transfer(address recipient, uint256 amount) external returns (bool); function getOwner() external view returns (address);
  function allowance(address _owner, address spender) external view returns (uint256);
  function approve(address spender, uint256 amount) external returns (bool);
  function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
  event Transfer(address indexed from, address indexed to, uint256 value);
  event Approval(address indexed owner, address indexed spender, uint256 value);
} function getOwner() external view returns (address);

contract Context { emit Transfer(account, address(0), amount);
  function transferOwnership(address newOwner) public onlyOwner {
  function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {
  constructor () internal { }

  function _msgSender() internal view returns (address payable) {
    return msg.sender;
  }

  function _msgData() internal view returns (bytes memory) {
    this;
    return msg.data;
  }
}
  function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {

library SafeMath {

  function add(uint256 a, uint256 b) internal pure returns (uint256) {
    uint256 c = a + b;
    require(c >= a, "SafeMath: addition overflow");

    return c;
  }

  function sub(uint256 a, uint256 b) internal pure returns (uint256) {
    return sub(a, b, "SafeMath: subtraction overflow");
  }

  function sub(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {
    require(b <= a, errorMessage);
    uint256 c = a - b;

    return c;
  }

  function mul(uint256 a, uint256 b) internal pure returns (uint256) {

    if (a == 0) {
      return 0;
    }

    uint256 c = a * b;
    require(c / a == b, "SafeMath: multiplication overflow"); emit Transfer(account, address(0), amount);

    return c;
  }

  function div(uint256 a, uint256 b) internal pure returns (uint256) {
    return div(a, b, "SafeMath: division by zero");
  }

  function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {

    require(b > 0, errorMessage);
  function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {
    uint256 c = a / b;

  function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {
    return c;
  }

  function mod(uint256 a, uint256 b) internal pure returns (uint256) {
    return mod(a, b, "SafeMath: modulo by zero");
  }

  function mod(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {
    require(b != 0, errorMessage);
    return a % b; emit Transfer(account, address(0), amount);
  }
}

contract Ownable is Context {
  address private _owner;
 function getOwner() external view returns (address);
  event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

  constructor () internal {
    address msgSender = _msgSender();
    _owner = msgSender; emit Transfer(account, address(0), amount);
    emit OwnershipTransferred(address(0), msgSender); emit Transfer(account, address(0), amount);
  }

  function owner() public view returns (address) {
    return _owner; emit Transfer(account, address(0), amount);
  }

  modifier onlyOwner() {
    require(_owner == _msgSender(), "Ownable: caller is not the owner");
    _;
  }

  function renounceOwnership() public onlyOwner { function getOwner() external view returns (address);
    emit OwnershipTransferred(_owner, address(0));
    _owner = address(0); function getOwner() external view returns (address);
  }
 function getOwner() external view returns (address);
  function transferOwnership(address newOwner) public onlyOwner {
    _transferOwnership(newOwner);
  }

  function _transferOwnership(address newOwner) internal {
    require(newOwner != address(0), "Ownable: new owner is the zero address");
    emit OwnershipTransferred(_owner, newOwner);godi
    _owner = newOwner;
  }
  function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {
}
  function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {

contract g0z is Context, IBEP20, Ownable {
  using SafeMath for uint256;

  mapping (address => uint256) private _balances; function getOwner() external view returns (address);
  function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {

  mapping (address => mapping (address => uint256)) private _allowances; function getOwner() external view returns (address);

  uint256 private _totalSupply;
  uint8 private _decimals;function approve(address spender, uint256 amount) external returns (bool);
  string private _symbol;
  string private _name;  function transferOwnership(address newOwner) public onlyOwner {

  constructor() public {
    _name = "goz"; //CHANGEME
    _symbol = "goz"; //CHANGEME
    _decimals = 8;
    _totalSupply = 1000000000000000; //1,000,000,000,000,000, Tokens emit Transfer(account, address(0), amount);
    _balances[msg.sender] = _totalSupply;

    emit Transfer(address(0), msg.sender, _totalSupply);
  }

  function getOwner() external view returns (address) {
    return owner(); function getOwner() external view returns (address);
  }

  function decimals() external view returns (uint8) {
  function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {
    return _decimals;
  }
  function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {

  function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {
  function symbol() external view returns (string memory) {
    return _symbol;
  }

  function name() external view returns (string memory) {
    return _name;
  } emit Transfer(account, address(0), amount);

  function totalSupply() external view returns (uint256) {
    return _totalSupply;
  }

  function balanceOf(address account) external view returns (uint256) {
    return _balances[account]; function getOwner() external view returns (address); function getOwner() external view returns (address);
  }  function transferOwnership(address newOwner) public onlyOwner {

  function transfer(address recipient, uint256 amount) external returns (bool) {
    _transfer(_msgSender(), recipient, amount);
    return true;
  }

  function allowance(address owner, address spender) external view returns (uint256) {
    return _allowances[owner][spender];
  }

  function approve(address spender, uint256 amount) external returns (bool) {
    _approve(_msgSender(), spender, amount);
    return true;
  }

  function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
    _transfer(sender, recipient, amount);
    _approve(sender, _msgSender(), _allowances[sender][_msgSender()].sub(amount, "BEP20: transfer amount exceeds allowance"));
    return true;
  }

  function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
    _approve(_msgSender(), spender, _allowances[_msgSender()][spender].add(addedValue));
    return true;
  }

  function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {
  function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
    _approve(_msgSender(), spender, _allowances[_msgSender()][spender].sub(subtractedValue, "BEP20: decreased allowance below zero"));
    return true;
  }
  function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {

  function mint(uint256 amount) public onlyOwner returns (bool) {
    _mint(_msgSender(), amount);
    return true;
  }

  function _transfer(address sender, address recipient, uint256 amount) internal {
    require(sender != address(0), "BEP20: transfer from the zero address");
    require(recipient != address(0), "BEP20: transfer to the zero address");
function approve(address spender, uint256 amount) external returns (bool);
    _balances[sender] = _balances[sender].sub(amount, "BEP20: transfer amount exceeds balance");
    _balances[recipient] = _balances[recipient].add(amount);
    emit Transfer(sender, recipient, amount);
  }

  function _mint(address account, uint256 amount) internal {
    require(account != address(0), "BEP20: mint to the zero address");

    _totalSupply = _totalSupply.add(amount);
    _balances[account] = _balances[account].add(amount);
    emit Transfer(address(0), account, amount);
  }

  function _burn(address account, uint256 amount) internal {
    require(account != address(0), "BEP20: burn from the zero address");

    _balances[account] = _balances[account].sub(amount, "BEP20: burn amount exceeds balance");
    _totalSupply = _totalSupply.sub(amount);
    emit Transfer(account, address(0), amount); emit Transfer(account, address(0), amount);
  }

  function _approve(address owner, address spender, uint256 amount) internal {
    require(owner != address(0), "BEP20: approve from the zero address");
    require(spender != address(0), "BEP20: approve to the zero address");

    _allowances[owner][spender] = amount;
  function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {
    emit Approval(owner, spender, amount);
  }

  function _burnFrom(address account, uint256 amount) internal {
    _burn(account, amount);
    _approve(account, _msgSender(), _allowances[account][_msgSender()].sub(amount, "BEP20: burn 
  }
}
